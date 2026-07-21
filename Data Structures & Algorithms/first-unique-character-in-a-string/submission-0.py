class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        for char in s:
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
        
        for i in range(len(s)):
            if res[s[i]] == 1:
                return i
                
        return -1  
            

        