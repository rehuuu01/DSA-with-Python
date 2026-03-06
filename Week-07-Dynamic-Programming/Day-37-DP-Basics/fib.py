
def fib(num,dp=[]):
    dp=[-1]*(num+1)
    if num<=1:
        return num
    if dp[num]!=-1:
        return dp[num]
    dp[num]= fib(num-1,dp)+fib(num-2,dp)
    return dp[num]

n=5
print(fib(n))


