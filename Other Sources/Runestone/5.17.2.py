# Write a recursive function to reverse a list.


def reverse(l):
    if len(l) == 0:
        return []
    return [l[-1]] + reverse(l[:-1])


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse(l))


# [9, 8, 7, 6, 5, 4, 3, 2, 1]
