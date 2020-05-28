T = int(input())

for testcase in range(T):
    N = int(input())
    max_speeds = input().split()
    max_speeds = [int(i) for i in max_speeds]
    actual_speeds = [max_speeds[0]]  # first one moves at maximum available speed
    for index in range(1, len(max_speeds)):
        actual_speeds.append(min([max_speeds[index], actual_speeds[index - 1]]))
    count = 0
    for index in range(len(max_speeds)):
        if max_speeds[index] == actual_speeds[index]:
            count += 1
    print(count)
