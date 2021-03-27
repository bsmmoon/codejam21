def solve(n, c):
    if c not in range (n-1, int((n*(1+n))/2)): return "IMPOSSIBLE"

    counts = []
    total = n-1  # all 1s initially
    for i in range(n-1):
        count = min(n - i, c - (total - 1))
        if count == 1: break
        counts.append(count)
        total += count - 1

    arr = list(range(1, n+1))[::-1]
    for count in counts[::-1]:
        arr = arr[:count][::-1] + arr[count:]
    arr = arr[::-1]

    return arr

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
