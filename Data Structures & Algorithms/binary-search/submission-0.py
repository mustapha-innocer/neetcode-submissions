class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            md = (l + r) // 2
            if target > nums[md]:
                l = md + 1
            elif target < nums[md]:
                r = md - 1
            else:
                return md
        return -1
        