import time


def fact(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)

    return result


def rec_fact(n):
    if n == 0:
        return 1
    return n * rec_fact(n - 1)


def fib(n):
    n1 = 0
    n2 = 1
    fib_n = 0
    for count in range(n - 1):
        fib_n = n2 + n1
        n1, n2 = n2, fib_n

    return fib_n


def rec_fib(n, memo):
    if n <= 2:

        return 1

    if n in memo:
        return memo[n]
    result = rec_fib(n - 1, memo) + rec_fib(n - 2, memo)
    memo[n] = result

    return result

#
# start = time.perf_counter_ns()
# print(fib(50))
# print(time.perf_counter_ns() - start)

# start = time.perf_counter_ns()
print(rec_fib(7, {}))
# print(time.perf_counter_ns() - start)
