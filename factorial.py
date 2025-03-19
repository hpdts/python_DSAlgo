import unittest
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def factorial2(n):
    res = 1
    def helper(count):
        nonlocal res
        if count > n:
            return
        res = res * count
        helper(count + 1)
        return res
    helper(1)
    return res

def factorial3(n):
    res = [1]
    def helper(count):
        if count > n:
            return
        res[0] *= count
        helper(count + 1)

    helper(1)
    return res[0]

assert factorial(3) == 6
assert factorial(5) == 120
assert factorial(8) == 40320
assert factorial2(3) == 6
assert factorial3(8) == 40320
print('All tests passed')