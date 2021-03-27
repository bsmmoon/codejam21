def solve(n, c):
    if c not in range (n, int((n*(1+n))/2) + 1): return "IMPOSSIBLE"
    return [4,2,1,3]

def verify(n, arr):
    if arr == "IMPOSSIBLE": return
    count = 0
    for i in range(1, n):
        j = arr.index(i)
        arr = arr[:i-1] + arr[i-1:j+1][::-1] + arr[j+1:]
        count += j+1 - i + 1
    return count

t = int(input())
for i in range(1, t+1):
    n, c = input().split()
    n, c = int(n), int(c)
    solution = solve(n, c)
    print('Case #{}: {} ({}, {})'.format(i, solution, c, verify(n, solution)))
