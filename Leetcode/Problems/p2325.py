import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters = string.ascii_lowercase
        sub = {" ": " "}
        # num_repeats = int(len(key) / 26) + 1
        # letters_expanded = (letters * num_repeats)[:]
        idx = 0
        for k in key:
            if k not in sub:
                sub[k] = letters[idx]
                idx += 1
        
        res = []
        for s in message:
            res.append(sub[s])
        return "".join(res)
