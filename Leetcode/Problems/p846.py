from collections import Counter, deque

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if not len(hand) % groupSize == 0:
            return False

        counts = Counter(hand)
        unique_nums = deque(sorted(list(set(hand))))


        while unique_nums:
            start = unique_nums.popleft()
            if counts[start] > 0:
                count_to_use = counts[start]
                for i in range(groupSize):
                    current_card = start + i
                    if counts[current_card] < count_to_use:
                        return False
                    counts[current_card] -= count_to_use

        return True

