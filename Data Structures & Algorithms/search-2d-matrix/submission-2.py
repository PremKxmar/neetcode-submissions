class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left,right=0,len(matrix)*len(matrix[0])-1
        n=len(matrix[0])
        while left<=right:
            mid=left+(right-left)//2
            row=mid//n
            col=mid%n
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                left=mid+1
            else:
                right=mid-1
        return False
    