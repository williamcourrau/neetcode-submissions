class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0
        right = 0
        char_set = set()
        longest_string = 0


        while right < len(s):
            right_char = s[right]
             
            if right_char not in char_set:
                char_set.add(right_char)
                right += 1
                longest_string = max(longest_string, right - left)
            else:
                # remove characters from the left one at a time,
                # only until the duplicate is gone — not the whole window
                char_set.remove(s[left])
                left += 1

        return longest_string


                 

            

