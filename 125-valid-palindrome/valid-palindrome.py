class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        b=""
        for i in s:
            if i.isalnum():
                b=b+i
        if b==b[::-1]:
            return True
        else:
            return False