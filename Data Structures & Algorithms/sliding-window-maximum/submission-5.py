class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        if len(nums)<k:
            return nums
        for i in range(0,len(nums)-k-1):
            arr=nums[i:i+k]
            l.append(max(arr))
        return l
