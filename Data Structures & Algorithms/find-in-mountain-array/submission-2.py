class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                left=mid+1
            else:
                right=mid-1
        peak=left
            
        left,right=0,peak
        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        
        left,right=peak+1,n-1
        while left<=right:
            mid=left+(right-left)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                right=mid-1
            else:
                left=mid+1
        return -1
