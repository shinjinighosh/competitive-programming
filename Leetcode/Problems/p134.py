# 134. Gas Station

'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        required = 0
        start = 0
        for i, g in enumerate(gas):
            current_gas += cost[i] - g
            if current_gas > 0:
                required += current_gas
                start = i + 1
                current_gas = 0
        if required + current_gas <= 0:
            return start
        return -1
