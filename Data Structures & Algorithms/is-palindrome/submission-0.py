class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        left = 0
        right = len(newStr) - 1

        while right > left:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1

        return True

        