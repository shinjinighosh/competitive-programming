T = int(input())

for testcase in range(T):
    activities, origin = input().split()
    laddus = 0
    activities = int(activities)
    for ac in range(activities):
        activity = input().split()
        if "CONTEST_WON" in activity:
            rank = int(activity[1])
            laddus += 300 + max([0, 20 - rank])
        elif "TOP_CONTRIBUTOR" in activity:
            laddus += 300
        elif "BUG_FOUND" in activity:
            laddus += int(activity[1])
        else:  # contest hosting
            laddus += 50
    if origin == "INDIAN":
        print(laddus // 200)
    else:  # Non-Indian
        print(laddus // 400)
