def tribonacci(n):
    if n >= 3:
        return tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
    else:
        if n==0:
            return 0
        else:
            return 1
print(tribonacci(5))
