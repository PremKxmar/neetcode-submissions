class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        max_len = 0
        mp = {}
        
        for right in range(len(s)):
            mp[s[right]] = mp.get(s[right], 0) + 1
            max_freq = max(max_freq, mp[s[right]])
            
            # If the number of replacements needed > k, shrink the window
            if (right - left + 1) - max_freq > k:
                mp[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len
