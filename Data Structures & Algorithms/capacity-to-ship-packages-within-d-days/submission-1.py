class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        mini=right
        while left<=right:
            weight=left+(right-left)//2
            sumx=0
            count=1
            for i in weights:
                if sumx+i<=weight:
                    sumx+=i
                else:
                    count+=1
                    sumx=i
            if count<=days:
                mini=min(mini,weight)
                right=weight-1
            else:
                left=weight+1
        return mini
            
            