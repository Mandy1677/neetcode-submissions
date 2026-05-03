class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need to find the pivot position in the array
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
        # we have found the pivot, which is index l

        # return the output, which is the minimum of the original array
        return nums[l]