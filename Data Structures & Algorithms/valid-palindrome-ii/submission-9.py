class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            if s[left] != s[right]:
                left_check=self.helper(s,left+1,right)
                right_check=self.helper(s,left,right-1)
                return left_check or right_check
            left+=1
            right-=1
        return True

    def helper(self,s,left,right):
        while left<right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True