class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        if len(nums)<3:
            return nums
        for i in range(0,len(nums)-2):
            arr=nums[i:i+3]
            l.append(max(arr))
        return l
