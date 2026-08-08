class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        def backtracking(start, subset):
            if start == len(nums):
                result.add(tuple(subset))
                return
            
            subset.append(nums[start])
            backtracking(start + 1, subset)
            subset.pop()
            backtracking(start + 1, subset)

        backtracking(0, [])
        return [list(s) for s in result]