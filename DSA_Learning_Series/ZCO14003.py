N = int(input())
budgets = []

for budget in range(N):
    budgets.append(int(input()))

budgets.sort(reverse=True)
max_revenue_earned = -1

for index, budget in enumerate(budgets):
    revenue = budget * (index + 1)
    if revenue > max_revenue_earned:
        max_revenue_earned = revenue

print(max_revenue_earned)
