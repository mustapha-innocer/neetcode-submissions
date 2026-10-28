class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in val_index:
                return [val_index[diff], i]
            val_index[v] = i
        return []
        