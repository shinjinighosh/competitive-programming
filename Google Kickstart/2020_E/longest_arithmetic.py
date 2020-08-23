T = int(input())

for testcase in range(T):

    N = int(input())
    arr = list(map(int, input().split()))

    max_len = 0
    current_diff = None
    curr_len = 0
    for i in range(len(arr) - 1):
        if current_diff is None:
            current_diff = arr[i + 1] - arr[i]
        if arr[i + 1] - arr[i] == current_diff:
            curr_len += 1
            # print(arr[i], curr_len)
            max_len = max(max_len, curr_len)
        else:
            current_diff = arr[i + 1] - arr[i]
            curr_len = 1
    print("Case #" + str(testcase + 1) + ": " + str(max_len + 1))
