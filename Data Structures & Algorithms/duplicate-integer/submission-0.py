class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for x in nums:
            if nums.count(x)>1:
                return True
        return False