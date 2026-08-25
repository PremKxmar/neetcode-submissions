class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[right]>nums[left]:
                if nums[left]==target:
                    return left
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>nums[left]:
                left=mid+1
            else:
                right=mid-1
        return -1