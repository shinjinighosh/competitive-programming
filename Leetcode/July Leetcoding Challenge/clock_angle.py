# Angle Between Hands of a Clock

'''
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs((hour % 12) * 30 + minutes / 2 - 6 * minutes)
        return min(angle, 360 - angle)
