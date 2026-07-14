class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_len=0
        mp={}
        for right in range(len(s)):
            if s[right] in mp and mp[s[right]]>=left:
                left=mp[s[right]]+1
            mp[s[right]]=right
            max_len=max(right-left+1,max_len)
        return max_len