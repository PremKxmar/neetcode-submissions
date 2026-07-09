class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=[]
        left,right=0,len(s)-1
        while left<right:
            
            if s[left].lower()!=s[right].lower():
                while len(l)<2 and left<right and len(l)<=1:
                    l.append(str(s[left]))
                    left+=1
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
            