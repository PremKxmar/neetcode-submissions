class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].lower() != s[right].lower():
                skip_left = self.is_palindrome(s, left + 1, right)
                return skip_left 
            
            left += 1
            right -= 1
        
        return True
    
    def is_palindrome(self, s, left, right):
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True