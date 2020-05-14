T = int(input())

for testcase in range(T):
    N = int(input())
    print("HOSTED" if N in [2010, 2015, 2016, 2017, 2019] else "NOT HOSTED")
