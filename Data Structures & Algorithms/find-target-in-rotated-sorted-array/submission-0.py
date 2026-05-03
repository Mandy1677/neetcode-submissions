class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        arr = nums[pivot:] + nums[:pivot]

        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return (mid + pivot) % len(nums)
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
        