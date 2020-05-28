# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.


def countBits(self, num: int) -> List[int]:
    result = []
    for i in range(num + 1):
        binary_form = bin(i)[2:]
        num_ones = binary_form.count('1')
        result.append(num_ones)
    return result
