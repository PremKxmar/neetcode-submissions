class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=[]
        left,right=0,len(s)-1
        count=0
        while left<right:
            if s[left].lower()!=s[right].lower() and count<2:
                    l.append(s[left])
                    count+=1
                    left+=1
                    right-=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
            