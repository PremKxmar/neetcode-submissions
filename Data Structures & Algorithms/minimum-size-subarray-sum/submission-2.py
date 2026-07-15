class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sumx=0
        min_length=float('inf')
        for right in range(len(nums)):
            sumx+=nums[right]
            while sumx>=target:
                min_length=min(min_length,right-left+1)
                sumx-=nums[left]
                left+=1
        return 0 if min_length==float('inf') else min_length