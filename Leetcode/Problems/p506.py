class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        indexed_scores = [(score[idx], idx) for idx in range(len(score))]
        sorted_indexed_scores = sorted(indexed_scores, reverse=True, key = lambda x: x[0])
        # now I have a list that looks like [(5, 0), (4, 1), ...]
        memo = {} # old_idx : position
        for idx, (score_num, old_idx) in enumerate(sorted_indexed_scores):
            memo[old_idx] =  idx
        res = []
        for new_idx in range(len(score)):
            pos = memo[new_idx] # new_idx and old_idx are the same
            if pos == 0:
                res.append("Gold Medal")
            elif pos == 1:
                res.append("Silver Medal")
            elif pos == 2:
                res.append("Bronze Medal")
            else:
                res.append(str(pos+1))
        return res
        
