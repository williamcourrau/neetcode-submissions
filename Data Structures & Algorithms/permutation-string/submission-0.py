class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            if c in s1_count:
                s1_count[c] += 1
            else:
                s1_count[c] = 1
        
        left = 0
        window = {}
        for right in range(len(s2)):
            c = s2[right]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1


            while right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                
                left+=1
            
            print("window:", window, "s1_count", s1_count)
            if window == s1_count:
                return True
        
        return False




