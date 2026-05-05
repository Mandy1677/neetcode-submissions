class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    res.append(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
            
        res = set(res)
        res = list(res)
        return res
            
            
