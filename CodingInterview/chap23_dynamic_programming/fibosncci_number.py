import collections


def my(n:int):
    dp = collections.defaultdict(int)
    def fibo(num):
        if num <=1:
            return num
        if dp[num]:
            return dp[num]
        dp[num] = fibo(num-1)+fibo(num-2)
        return dp[num]
    return fibo(n)

def brute_force(N:int)->int:
    if N<=1:
        return N
    return brute_force(N-1)+brute_force(N-2)

def memoization(N:int)->int:
    dp = collections.defaultdict(int)
    def fib(N:int)->int:
        if N<=1:
            return N
        if dp[N]:
            return dp[N]
        dp[N]=fib(N-1)+fib(N-2)
        return dp[N]

def tabulation(N:int)->int:
    dp = collections.defaultdict(int)
    def fib(N:int)->int:
        dp[1]=1
        for i in range(2,N+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[N]

def fib(N:int)->int:
    x,y = 0,1
    for i in range(0,N):
        x,y=y,x+y
    return x




answer = my(5)
print(answer)