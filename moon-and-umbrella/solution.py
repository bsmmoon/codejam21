class Progress:
    def __init__(self, prev):
        self.prev = prev
        if prev == "C":
            self.c, self.j = 0, False
        elif prev == "J":
            self.c, self.j = False, 0
        else:
            self.c, self.j = 0, 0

    def __repr__(self):
        return "{}, {}, {}".format(self.c, self.j, self.prev)

def solve(x, y, s):
    p = Progress(s[0])

    for c in s[1:]:
        if c == "C":
            if p.prev == "J": p.c = p.j + y
            p.j = False
        elif c == "J":
            if p.prev == "C": p.j = p.c + x
            p.c = False
        elif c == "?":
            if p.prev == "C":
                p.j = p.c + x
            elif p.prev == "J":
                p.c = p.j + y
            else:
                p.c = min(p.c, p.j + y)
                p.j = min(p.c + x, p.j)
        p.prev = c
    if p.c is False: return p.j
    if p.j is False: return p.c
    return min(p.c, p.j)

t = int(input())
for i in range(1, t+1):
    x, y, s = input().split(" ")
    x = int(x)
    y = int(y)
    print('Case #{}: {}'.format(i, solve(x, y, s)))
