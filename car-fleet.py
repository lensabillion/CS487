class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        print(cars)
        print(times)
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: 
                ans += 1
            else: 
                times[-1] = lead
        return ans + bool(times)
