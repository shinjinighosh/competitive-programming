class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        count = 0
        taken_indices = set()
        for idx, wt in enumerate(people):
            if idx not in taken_indices:
                rem = limit - wt
                j = len(people)
                while people[j] <= wt:
                    j -= 1
                j += 1
                if j < len(people):
                    
