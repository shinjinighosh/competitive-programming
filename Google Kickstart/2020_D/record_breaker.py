T = int(input())

for testcase in range(T):
    N = int(input())
    V = list(map(int, input().split()))
    record = 0
    current_max = -1
    for i in range(len(V)):
        if V[i] > current_max:
            current_max = V[i]
            if i == len(V) - 1 or V[i] > V[i + 1]:
                record += 1
    print(f"Case #{testcase+1}: {record}")

'''
Problem
Isyana is given the number of visitors at her local theme park on N consecutive days. The number of visitors on the i-th day is Vi. A day is record breaking if it satisfies both of the following conditions:
The number of visitors on the day is strictly larger than the number of visitors on each of the previous days.
Either it is the last day, or the number of visitors on the day is strictly larger than the number of visitors on the following day.
Note that the very first day could be a record breaking day!

Please help Isyana find out the number of record breaking days.
'''
