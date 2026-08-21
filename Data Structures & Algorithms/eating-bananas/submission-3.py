class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        count=right

        while left<=right:
            hours=0
            k=left+(right-left)//2
            for i in piles:
                hours+=math.ceil(i/k)
            if hours<=h:
                count=k
                right=k-1
            else:
                left=k+1
        return count

                        


        