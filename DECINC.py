# Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

# Input: First line will contain a number N.
# Output: Output a single line, the new value of the number.

N = int(input())
print(N + 1 if N % 4 == 0 else N - 1)
