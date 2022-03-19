import mosek
import sys
import numpy as np
from util.calc_c import calc_c
from util.calc_q_o import get_q_input_for_mosek, calc_q_o
inf = np.inf
# Define a stream printer to grab output from MOSEK
def streamprinter(text):
    """
    わからん
    """
    sys.stdout.write(text)
    sys.stdout.flush()

def calc_node_point(node_cnt, exp):
    """
    数式の最小化を行うことでノードの座標を計算。
    Parameters
    ----------
    exp : 
        数式
    Returns
    -------
    fruit_price : int
        対象の果物の値段。
    consumption_tax : int
        消費税値。
    """
    with mosek.Env() as env:
        # よくわからん
        with env.Task() as task:
            # よくわからん
            # task.set_Stream(mosek.streamtype.log, streamprinter)

            # まず、変数の制約を諸々書く。
            # 変数の個数
            numvar = node_cnt
            # 変数に関しての制約
            bkx = [mosek.boundkey.lo] * numvar
            blx = [0.0] * node_cnt
            bux = [inf] * node_cnt

            task.appendvars(numvar)
            # 変数の一次の式の係数を書く。
            c = calc_c(node_cnt, exp)
            for j in range(numvar):
                task.putcj(j, c[j])
                task.putvarbound(j, bkx[j], blx[j], bux[j])

            # 次に、二次の項について係数を入力
            q_o = calc_q_o(node_cnt, exp)
            qsubi, qsubj, qval = get_q_input_for_mosek(node_cnt, q_o)

            task.putqobj(qsubi, qsubj, qval)

            task.putobjsense(mosek.objsense.minimize)

            task.optimize()

            # Print a summary containing information
            # about the solution for debugging purposes
            # task.solutionsummary(mosek.streamtype.msg)

            solsta = task.getsolsta(mosek.soltype.itr)

            # Output a solution
            xx = [0.] * numvar
            task.getxx(mosek.soltype.itr,
                       xx)

            if solsta == mosek.solsta.optimal:
                print("Optimal solution: %s" % xx)
            elif solsta == mosek.solsta.dual_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif solsta == mosek.solsta.prim_infeas_cer:
                print("Primal or dual infeasibility.\n")
            elif mosek.solsta.unknown:
                print("Unknown solution status")
            else:
                print("Other solution status")
    return np.array(xx)