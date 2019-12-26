##https://leetcode.com/problems/n-th-tribonacci-number/submissions/

res = [None] * 40

def tribonacci(n):
    if res[n] != None:
        return res[n]
    if n >= 3:
        res[n] = tribonacci(n-3)+tribonacci(n-2)+tribonacci(n-1)
        return res[n]
    else:
        if n==0:
            return 0
        else:
            return 1
## slow
        
def oldtribonacci(n):
    if n >= 3:
        return oldtribonacci(n-3)+oldtribonacci(n-2)+oldtribonacci(n-1)
    else:
        if n==0:
            return 0
        else:
            return 1

