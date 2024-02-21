from math import comb
from itertools import combinations


def ch(n, r):
    try:
        return comb(n, r)
    except:
        return 0


def h(n, r):
    return ch(n + r - 1, r)


def k(r):
    return h(N, r)


# x1 + x2 + ... + xN = R
# L1 <= x1 < R1
# L2 <= x2 < R2
# ...
# LN <= xN < RN4

N = 26
listL = [2008, 5828, 2933, 411, 4223, 1614, 5679, 6349, 117, 2321, 2281, 1939, 6273, 1477, 800, 4727, 2828, 1782, 1744,
         2486, 6312, 2188, 5380, 1772, 2708, 1528]
listU = [67434882, 35387831, 30133881, 63609725, 18566959, 25526751, 44298843, 26793895, 40292840, 42293336, 26301527,
         50793633, 51546489, 36871159, 65314188, 15882817, 40562779, 48186923, 37382713, 56149154, 18170199, 63940428,
         58244044, 29193116, 22309445, 40848052]
R = 69696969

# For sum(x1+...+xN) = R with limits 0<=x<=R, the answer is (N+R-1) choose (R).
# For sum(x1+...+xN) = R with limits Li<=x<=R, we subtract Li from each limit and also subtract sum(Li) from R, then apply the same formula.

D = R - sum(listL)
listV = [listU[x] - listL[x] for x in range(N)]

# For sum(x1+...+xN) = R with limits 0<=x<=D, we calculate number of solutions with limits 0<=x<=R and then subtract the solutions that we don't want.
# We do this by the principle of inclusion-exclusion.

M = 0
for i in range(1, N + 1):
    P = 0
    listComb = list(combinations(listV, i))
    # print(listComb)
    for j in listComb:
        # print(f"j = {j}")
        P += k(D - sum(j))
        # print(f"P = {P}")
    M += ((-1) ** i) * P
    # print(f"i = {i}")
    # print(f"M = {M}")
    print(f"Progress Report {i}/26")

Answer = k(D) + M
# Answer = 752430469455330072491758677550514904817745703296600879168009163798024721359209897523073437096956295928297471174278331932211282703732931794750953231296792847134818780387425
print(Answer)
print(Answer % 69696969)
