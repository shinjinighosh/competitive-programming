# Pascal’s triangle is a number triangle with numbers arranged in staggered rows such that

# anr=n!*r!/(n−r)!

# This equation is the equation for a binomial coefficient. You can build Pascal’s triangle by adding the two numbers that are diagonally above a number in the triangle. An example of Pascal’s triangle is shown below.
#
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
# Write a program that prints out Pascal’s triangle. Your program should accept a parameter that tells how many rows of the triangle to print.


def printPascal(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    for row in range(n):
        for pos in range(row + 1):
            if (pos == 0 or pos == row):
                arr[row][pos] = 1
                print(arr[row][pos], end=" ")
            else:
                arr[row][pos] = arr[row - 1][pos - 1] + arr[row - 1][pos]
                print(arr[row][pos], end=" ")
        print("\n", end="")


printPascal(5)
