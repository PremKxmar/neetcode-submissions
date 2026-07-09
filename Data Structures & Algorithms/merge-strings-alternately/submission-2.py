class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left1,left2=0,0
        s=""
        while left1<len(word1) and left2<len(word2):
            s+=word1[left1]
            s+=word2[left2]
            left1+=1
            left2+=1
        while left1<len(word1):
            s+=word1[left1]
            left1+=1
        while left2<len(word2):
            s+=word2[left2]
            left2+=1
        return s