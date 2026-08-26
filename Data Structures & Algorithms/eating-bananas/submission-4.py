class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        maxi=right
        while left<=right:
            k=left+(right-left)//2
            sumx=0
            for i in piles:
                sumx+=math.ceil(float(i)/k)
            if sumx<=h:
                maxi=k
                right=mid-1
            else:
                left=mid+1
        return maxi
