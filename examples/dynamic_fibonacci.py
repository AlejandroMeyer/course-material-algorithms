def fib_dp(n):
    dpf = [0] * (n+1)
    dpf[1] = 1
    for i in range(2, n+1):
        dpf[i] = dpf[i-1] + dpf[i-2]
    return dpf[n]