class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        hour_degree = minutes / 12 + (hour * 5)
        clock_degree = abs(hour_degree - minutes)
        res = clock_degree* 6
        return 360 - res if res > 180 else res
