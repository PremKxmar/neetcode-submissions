class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left1,left2=0,0
        result=[]
        while left1<len(word1) and left2<len(word2):
            result.append(word1[left1])
            result.append(word2[left2])
            left1+=1
            left2+=1
        result.append(word1[left1:])
        result.append(word2[left2:])
        return ''.join(result)