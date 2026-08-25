class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        left,right=k-1,len(nums)-1

        while k>0:
            nums[left],nums[right]=nums[right],nums[left]
            left-=1
            right-=1
            k-=1
        return nums
            