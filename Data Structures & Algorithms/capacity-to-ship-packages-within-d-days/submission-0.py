class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        result=right

        def canShip(capacity):
            ships=1
            current_capacity=capacity
            for i in weights:
                if current_capacity-i<0:
                    ships+=1
                    if ships>days:
                        return False
                    current_capacity=capacity
                current_capacity-=i
            return True


        while left<=right:
            capacity=left+(right-left)//2
            if canShip(capacity):
                result=min(result,capacity)
                right=capacity-1
            else:
                left=capacity+1
        return result