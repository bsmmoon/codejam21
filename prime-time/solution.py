# Assumptions
# It is ALWAYS better to do min number of appends
# It is ALWAYS better to do append with min digit
# Need minimally same length of digits

# Approach 1.

def digits(num):
    return len(str(num))

def solve(n, arr):
    count = 0
    for i, num in enumerate(arr):
        if i == 0: continue
        
        prev = arr[i-1]
        
        pprefix = int(str(prev)[:digits(num)])

        if prev < num:
            prev = num
            continue
        
        if prev == num:
            num *= 10
            count += 1
        
        elif pprefix == num:
            count += digits(prev) - digits(num)
            num = prev + 1
            
            if str(prev)[0] != str(num)[0]:
                num = prev * 10
                count += 1
        
        elif pprefix < num:
            diff = digits(prev) - digits(num)
            num *= pow(10, diff)
            count += diff
            
        elif pprefix > num:
            diff = digits(prev) - digits(num) + 1
            num *= pow(10, diff)
            count += diff
        
        arr[i] = num
        prev = num

    return count

t = int(input())
for i in range(1, t+1):
    n = int(input())
    arr = list(map(lambda x: int(x), input().split(" ")))
    print('Case #{}: {}'.format(i, solve(n, arr)))
