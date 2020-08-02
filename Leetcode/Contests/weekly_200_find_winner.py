# 5476. Find the Winner of an Array Game

'''
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
'''

# TO COMPLETE/CORRECT


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        past_winner = -1
        won_rounds = 0
        while won_rounds <= k:
            if arr[0] > arr[1]:
                # print("winner arr[0]", arr[0], "won_rounds", won_rounds)
                # arr[-1], arr[1] = arr[1], arr[-1]
                temp = arr.pop(1)
                arr.append(temp)
                if arr[0] == past_winner:
                    won_rounds += 1
                    # if arr[0] > arr[1]:
                    # will win all the rest
                    # return arr[0]
                else:
                    won_rounds = 1
                    past_winner = arr[0]
            else:  # new winner
                # print("winner arr[1]", arr[1], "won_rounds", won_rounds)
                # arr[-1], arr[1] = arr[1], arr[-1]
                # arr[0], arr[-1] = arr[-1], arr[0]
                temp = arr.pop(0)
                arr.append(temp)
                if arr[0] == past_winner:
                    won_rounds += 1
                else:
                    won_rounds = 1
                    past_winner = arr[0]
        return past_winner
