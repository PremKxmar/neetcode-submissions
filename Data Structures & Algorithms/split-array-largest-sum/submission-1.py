class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(largest):
            sumx=0
            count=1
            for i in nums:
                if sumx+i<=largest:
                    sumx+=i
                else:
                    sumx=i
                    count+=1
                    if count>k:
                        return False
            return True
            
            
        left=max(nums)
        right=sum(nums)
        mini=right
        while left<=right:
            mid=left+(right-left)//2
            if cansplit(mid):
                mini=mid
                right=mid-1
            else:
                left=mid+1
        return mini

        