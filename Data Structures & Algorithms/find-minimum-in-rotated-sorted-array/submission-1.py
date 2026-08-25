class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mini=float('inf')
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<mini:
                mini=nums[mid]
                right=mid-1
            else:
                left=mid+1
        return mini