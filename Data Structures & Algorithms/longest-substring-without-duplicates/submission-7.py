class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        longest_str = 0

        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            
            longest_str = max(longest_str, right - left + 1)
        
        return longest_str


            

        