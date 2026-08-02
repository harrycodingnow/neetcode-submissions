class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                res += char

        left = 0
        right = len(res) - 1

        while left < right:
            if res[left] == res[right]:
                left += 1
                right -= 1
            else:
                return False                
        
        return True
        

        