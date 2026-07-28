class Solution:
    def characterReplacement(self, s: str, k: int) -> int:                
        char_count = {}
        res = 0
        left = 0        
 
        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            while (i - left + 1) - max(char_count.values()) > k:
                char_count[s[left]] -= 1
                left += 1            
            res = max(res, (i - left + 1))
            
        return res

            

        

        