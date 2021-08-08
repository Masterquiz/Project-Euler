import functools

def Factorial_digit_sum(n):
    fac = functools.reduce(
            lambda a, b: a*b,
            [num for num in range(1, n)]
            )
    res = functools.reduce(
            lambda a, b: a+b,
            [int(d) for d in str(fac)]
            )
    return res


def Power_digit_sum(n):
    res = functools.reduce(
            lambda a, b: a+b,
            [int(d) for d in str(2**n)]
            )
    return res
