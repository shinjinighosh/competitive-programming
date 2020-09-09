import time
import random

# Set up a random experiment to test the difference between a sequential search and a binary search on a list of integers.


# binary search
def binarySearch(l, target):
    first = 0
    last = len(l) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if l[middle] == target:
            found = True
        else:
            if target < l[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return found


overall_start = time.time()

binary_search_time = 0
sequential_search_time = 0
num_expt = 100000

# for every experiment
for experiment in range(num_expt):
    # generate random list of 100 integers from the range 1 to 10^7
    randomlist = random.sample(range(1, 10000000), 100)
    randomlist.sort()

    # pick random number to search from range 1 to 10^7
    target = random.choice(range(1, 10000000))

    # record sequential and binary search times
    seq_start = time.time()
    for i in randomlist:
        if i == target:
            seq_end = time.time()
            break
    else:
        seq_end = time.time()

    sequential_search_time += seq_end - seq_start

    bin_start = time.time()
    found = binarySearch(randomlist, target)
    bin_end = time.time()

    binary_search_time += bin_end - bin_start


overall_end = time.time()

# return results
print("Time taken for", num_expt, "experiments in sequential search is",
      sequential_search_time, "and binary search is", binary_search_time)
print("Overall time taken is", overall_end - overall_start)
