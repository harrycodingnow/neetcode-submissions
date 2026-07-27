class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                cleaned_s += char
        left = 0
        right = len(cleaned_s) - 1

        while left < right:
            if cleaned_s[left] == cleaned_s[right]:
                left += 1
                right -=1
            else:
                return False
        
        return True
                
        



        
        