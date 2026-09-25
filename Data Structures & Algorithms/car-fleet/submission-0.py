class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        travel = []
        for x, v in zip(position, speed):
            travel.append([x, v])
        travel.sort()
        
        closestx, closestv = travel[-1]
        time1 = (target - closestx)/closestv
        time.append(time1)
        for i in range(len(travel) - 2, -1, -1):
            position, speed = travel[i]
            target_time = (target - position)/speed
            if target_time > time[-1]:
                time.append(target_time)
        return len(time)                


        