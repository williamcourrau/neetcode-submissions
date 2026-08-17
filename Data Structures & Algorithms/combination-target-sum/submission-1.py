class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(combination, index):
            
            if sum(combination) == target:
                result.append(combination[:])
                return
            elif sum(combination) > target:
                return
            
            for i in range(index, len(nums)):
                combination.append(nums[i])
                backtracking(combination, i)
                combination.pop()
        

        backtracking([], 0)
        return result