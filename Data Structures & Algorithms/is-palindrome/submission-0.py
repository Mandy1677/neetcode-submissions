class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        res = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                res += char
        left, right = 0, len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True
        