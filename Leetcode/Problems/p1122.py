class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arr1_ctr = Counter(arr1)
        arr2_set = set(arr2)
        for elt in arr2:
            res += [elt] * arr1_ctr[elt]
        other_elts = set(arr1) - set(arr2)
        other_elts_sorted = sorted(list(other_elts))
        for elt in other_elts_sorted:
            res += [elt] * arr1_ctr[elt]
        return res 
