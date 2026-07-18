from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans=[float('inf'),-1]
        formed=0
        left=0
        mp={}
        count=Counter(t)
        required=len(count)
        for right in range(len(s)):
            mp[s[right]]=mp.get(s[right],0)+1
            if s[right] in count and mp[s[right]]==count[s[right]]:
                formed+=1
            while formed==required:
                if right-left+1<ans[0]:
                    ans[0]=right-left+1
                    ans[1]=left
                mp[s[left]]-=1
                if s[left] in count and mp[s[left]]<count[s[left]]:
                    formed-=1
                left+=1
        if ans[0]==float('inf'):
            return ""
        return s[ans[1]:ans[0]+ans[1]]
                

