class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True
        
        def dfs(i):
            if i >= len(s):
                result.append(part[:])
                return
            
            for r in range(i, len(s)):
                if isPali(i, r):
                    part.append(s[i : r + 1])
                    dfs(r + 1)
                    part.pop()
        dfs(0)

        return result
