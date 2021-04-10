import functools
from fractions import gcd

class Solver:
    def solve(self, q, papers):
        max_ans = [""] * q
        max_exp = [0] * q
        for paper, score in papers:
            for i, ans in enumerate(list(paper)):
                if max_exp[i] < score:
                    max_exp[i] = score
                    max_ans[i] = ans
        total = functools.reduce(lambda a, b: a + b, max_exp)
        div = gcd(total, q)
        return ("".join(max_ans), total / div, q / div)

lines = iter("""4
1 3
FFT 3
1 3
FFT 2
2 6
FFTTTF 2
FTFTFT 4
2 2
FF 1
TT 1""".split("\n"))

import sys
def readline():
    return sys.stdin.readline()
    # return next(lines)

solver = Solver()
t = int(readline())
for i in range(1, t+1):
    n, q = map(lambda x: int(x), readline().split(" "))

    papers = []
    for _ in range(n):
        answer, score = readline().split(" ")
        papers.append((answer, int(score)))
    
    ans = solver.solve(q, papers)
    print('Case #{}: {} {}/{}'.format(i, ans[0], int(ans[1]), int(ans[2])))
