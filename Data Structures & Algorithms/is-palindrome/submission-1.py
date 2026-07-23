class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for char in s:
            if char.isalnum():
                cleaned_s += char
        cleaned_s = cleaned_s.lower()

        left = 0
        right = len(cleaned_s) - 1

        while right >= left:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        return True




        