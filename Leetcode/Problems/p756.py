class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowed_dict = defaultdict(set)
        for pattern in allowed:
            allowed_dict[(pattern[0], pattern[1])].add(pattern[2])

        def build(next_bottom, current, idx):
            if len(current) == 1: # at the top
                return True
            if idx == len(current) - 1:
                return build("", next_bottom, 0)
            for c in allowed_dict[(current[idx], current[idx+1])]:
                if build(next_bottom + c, current, idx + 1):
                    return True
            return False
        
        return build("", bottom, 0)
