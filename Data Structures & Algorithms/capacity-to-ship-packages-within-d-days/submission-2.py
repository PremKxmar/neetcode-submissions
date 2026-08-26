class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        maxi=right
        while left<=right:
            weight=left+(right-left)//2
            sumx=0
            count=1
            for i in weights:
                if sumx+i<=weight:
                    sumx+=i
                else:
                    sumx=i
                    count+=1
            if count<=days:
                maxi=weight
                right=weight-1
            else:
                left=weight+1
        return maxi
            