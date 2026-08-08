class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        picked = [False] * len(nums) # recall 

        def backtracking(start, subset):
            if len(subset) == len(nums):
                result.append(subset[:])
                return
            
            for i in range(start, len(nums)):
                if not picked[i]:
                    subset.append(nums[i])
                    picked[i] = True
                    backtracking(start, subset)
                    
                    picked[i] = False
                    subset.pop()
        
        backtracking(0, [])
        return result
