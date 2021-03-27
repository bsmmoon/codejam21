def solve(n, arr):
    count = 0
    for i in range(1, n):
        j = arr.index(i)
        arr = arr[:i-1] + arr[i-1:j+1][::-1] + arr[j+1:]
        count += j+1 - i + 1
    return count

t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    print('Case #{}: {}'.format(i, solve(n, arr)))
