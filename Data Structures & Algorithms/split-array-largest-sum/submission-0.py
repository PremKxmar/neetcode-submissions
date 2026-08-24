class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            currSum=0
            subArrays=1
            for i in nums:
                currSum+=i
                if currSum>largest:
                    subArrays+=1
                    currSum=i
                    if subArrays>k:
                        return False
            return True
        
        left=max(nums)
        right=sum(nums)
        result=right
        while left<=right:
            mid=left+(right-left)//2
            if canSplit(mid):
                result=mid
                right=mid-1
            else:
                left=mid+1
        return result   

