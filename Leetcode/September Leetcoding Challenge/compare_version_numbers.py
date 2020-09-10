# Compare Version Numbers

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
'''


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        while i < len(v1) and i < len(v2):
            a = int(v1[i])
            b = int(v2[i])
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                i += 1
        if i < len(v1):
            for k in range(i, len(v1)):
                if int(v1[k]) != 0:
                    return 1
            return 0
        elif i < len(v2):
            for k in range(i, len(v2)):
                if int(v2[k]) != 0:
                    return -1
            return 0
        else:
            return 0
