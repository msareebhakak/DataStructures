#
# Author: Sareeb Hakak
# Purpose: Practice recursion
# Date: 03 March 24
#

# 1. Divide a big problem into small, simple problem. Look for patterns
# 2. Find a base condition with simple answer (return that)
# 3. Return base condition answer to solve all sub problems

def find_sum(n):
    # find sum of numbers up to n
    add = 0
    if n == 1:
        add = 1
    else:
        add += n + find_sum(n - 1)
    return add


def factorial(n):
    # get the factorial of a non-negative integer
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


def get_fibonacci_at(n):
    # Define a function named fibonacci that calculates the nth Fibonacci number
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return get_fibonacci_at(n-1) + get_fibonacci_at(n-2)


if __name__ == '__main__':
    print(find_sum(6))
    print(get_fibonacci_at(6))
    print(factorial(5))
