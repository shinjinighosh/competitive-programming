N = int(input())

bracket_expression = input().split()
bracket_expression = [int(i) for i in bracket_expression]

nesting_depths = []
current_depth = 0

for element in bracket_expression:
    if element == 1:
        current_depth += 1
    else:
        current_depth -= 1
    nesting_depths.append(current_depth)

# print(nesting_depths)
max_depth = max(nesting_depths)
first_deep_nested = nesting_depths.index(max_depth) + 1 # because 1-indexed

print(f"{max_depth} {first_deep_nested}")
