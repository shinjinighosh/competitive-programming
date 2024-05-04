class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split(".")]
        v2 = [int(i) for i in version2.split(".")]

        if len(v1) < len(v2):
            v1.extend([0] * (len(v2) - len(v1)))
        elif len(v2) < len(v1):
            v2.extend([0] * (len(v1) - len(v2)))

        for a, b in zip(v1, v2):
            if a < b:
                return -1
            elif b < a:
                return 1
        
        return 0

