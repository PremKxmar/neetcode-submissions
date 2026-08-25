class Solution:
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            while not s[left].isalnum():
                left+=1
            while not s[right].isalnum():
                right-=1
            if s[left].lower()!=s[right].lower():
                return False
        return True