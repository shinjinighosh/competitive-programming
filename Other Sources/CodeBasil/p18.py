# Fibonacci Series


def findNthFibonacciTerm(n, memo=None):
	"""
	Args:
		{int} n
	Returns:
		{int} The nth term.
	"""
	# Write your code here.
  if memo is None:
    memo = {}
  if n in [0, 1]:
    memo[0] = 0
    memo[1] = 1
  if n not in memo:
    memo[n] = findNthFibonacciTerm(n-1, memo) + findNthFibonacciTerm(n-2, memo)
  return memo[n]
