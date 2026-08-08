class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for i in range(len(nums)):
            if nums[i] in memo:
                return True
            else:
                memo.add(nums[i])
        
        return False

        