class Solution:
    def finalPrices(self, prices):
        actual = []
        for i in range(len(prices)):
            j = i + 1
            flag = False
            while j < len(prices):
                print(i, j)
                if prices[j] <= prices[i]:
                    actual.append(prices[i] - prices[j])
                    flag = True
                    break
                j += 1
            # if j < len()
            if not flag:  # no discount
                actual.append(prices[i])
            print(actual)
        return actual
        # return actual


test = Solution()
prices = [8, 4, 6, 2, 3]
print(test.finalPrices(prices))
