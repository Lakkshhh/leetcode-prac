class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     low = 0
        #     high = len(matrix[i])-1

        #     while low <= high:
        #         mid = low + (high-low)//2

        #         if target < matrix[i][mid]:
        #             high = mid - 1
        #         elif target > matrix[i][mid]:
        #             low = mid + 1
        #         else:
        #             return True
        
        # return False

        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows*columns - 1

        while left <= right:
            mid = left + (right-left)//2

            row = mid // columns
            col = mid % columns

            if target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                return True
        
        return False