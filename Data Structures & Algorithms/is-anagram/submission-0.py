class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the len of both words are the same.
        # compute the first word save into a dicitonary {a : 2, b : 3, d : 4}
        # check the second word: 

        if len(s) != len(t):
            return False
        
        memory = {}
        for i in range(len(s)):
            if s[i] in memory:
                memory[s[i]]+=1
            else:
                memory[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in memory:
                return False
            else:
                memory[t[i]]-=1

        for value in memory.values():
            if value != 0:
                return False

        return True

            

        