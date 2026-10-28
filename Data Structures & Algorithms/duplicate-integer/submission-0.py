class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if count_dict.get(num) is None:
                count_dict[num] = 1
            else:
                count_dict[num] += 1
        
        for _, val in count_dict.items():
            if val > 1:
                return True
        return False