class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write=0
        scan=1
        while scan<=(len(nums)-1):
            if nums[scan]!=nums[write]:
                write+=1
                nums[write]=nums[scan]
                scan+=1
            else:
                scan+=1
        return write+1
