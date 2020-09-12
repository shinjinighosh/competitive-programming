# Write a recursive function to compute the factorial of a number.

# factorial(n) = 1 * 2 * ... * (n-1) * n


def factorial(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = n * factorial(n - 1, memo)
        return memo[n]


memo = {}
print(factorial(8, memo))
print(memo)
