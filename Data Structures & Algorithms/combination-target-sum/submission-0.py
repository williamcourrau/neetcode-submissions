class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(subset, start, current_sum):
            if current_sum > target:
                return
            
            if current_sum == target:
                result.append(subset[:])
                return 
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i, current_sum + nums[i])
                subset.pop()
            
        backtrack([], 0, 0)
        return result
            