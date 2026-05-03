class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            if hours > h:
                return False
            return True
        minK = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r)//2
            if canFinish(mid):
                minK = mid
                r = mid - 1
            elif not canFinish(mid):
                l = mid + 1
        return minK
        