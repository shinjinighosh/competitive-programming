'''
554. Brick Wall

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2

|-|--|--|-|
|---|-|--|
|-|---|--|

in a matrix of n*m, we have some k pairs (i, j) that represent a gap with 1 and 0 otherwise. we want to make a cut s.t. for every j and i = 0 to n, sum(j) += matrix(i, j). The sum represents no of gaps and so max(sum(j)) where j = 0..m

cumulative: [[1,3,5,6],
             [3,4,6],
             [1,4,6],
             [2,6],
             [3,4,6],
             [1,4,5,6]
              ]

Understand:
- total same width rows
- choose an x value that goes through a brick least number of times
- "goes through" if cumulative[i] < x < cumulative[i+1] for some i in the row
- we are given widths, so we need to get a running cumulative sum to get the x values of where each brick ends
- answer: an x value for which sum(if(cumu[i] < x < cumu[i+1]) for all rows) is least
- equivalently, we can count the number of edges we are going through and maximize that, i.e., choose x for which sum(# of edges crossed) is max

Match:
- want to go through the most edges (represented by the cumulative sums)
- hashmap
  key: cumulative sum (within a row)
  value: count
[1,2,2,1]
sum: 1+2+2+1
[3,1,2]
sum: 0+3

1: 1
3: 2
5: 1
6: 1

Plan/Pseudocode

1. Convert input array to hashmap
2. Iterate over the hashmap, get the max count
3. Len(input) - max count = Min bricks crossed

hashmap -> collections.defaultdict(int)
loop over input array
  cum_sum = 0
  loop over length(row) - 1
    cum_sum += row[idx]
    hashmap[cum_sum] += 1

max_count = -float("inf")
loop over hashmap
  if val > max_count:
      max_count = val

return len(input) - max_count

Edge Cases
1. [[]]



'''
import collections


def least_bricks(wall):
    edge_count = collections.defaultdict(int)
    for row in wall:
        row_sum = 0
        for edge in row[:-1]:
            row_sum += edge
            edge_count[row_sum] += 1

    return len(wall) - max(edge_count.values()) if (len(edge_count) > 0) else len(wall)
    # return (len(edge_count) > 0) len(wall) - max(edge_count.values()) : len(wall)

    # max_count = 0
    # for edge in edge_count:
    #   max_count = max(max_count, edge_count[edge])

    # return len(wall) - max_count


def test1():
    wall1 = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    print(least_bricks(wall1))


def test2():
    wall2 = [[3], [3], [3]]
    print(least_bricks(wall2))


'''
Review:
Test Case 1
[[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]

cumulative: [[1,3,5,6],
             [3,4,6],
             [1,4,6],
             [2,6],
             [3,4,6],
             [1,4,5,6]
              ]
edge_count:
row 1 {1: 1, 3:1, 5:1}
row 2 {1:1, 3:2, 4:1, 5:1}
row 3 {1:2, 3:2, 4:2, 5:1}
row 4 {1:2, 2:1, 3:2, 4:2, 5:1}
row 5 {1:2, 2:1, 3:3, 4:3, 5:1}
row 6 {1:3, 2:1, 3:3, 4:4, 5:2}

return 6 - 4 -> 2

Test Case 2:
[[6], [6], [6]]
edge_count = {}
return 3


Evaluation:
len(wall) is O(n)
sum(row) / num bricks per row is O(k)

time O(nk)
space O(k)
'''
