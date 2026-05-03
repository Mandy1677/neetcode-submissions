class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # follow the vertical order of the first one until we find the row we're looking for
        m = len(matrix)
        n = len(matrix[0])
        rowhead = 0
        target_m = m - 1
        for i in range(m):
            rowhead = matrix[i][0]
            if rowhead > target:
                target_m = i-1
                break
            elif rowhead == target:
                return True
        

        # go down the row until we find the num/not find it
        for i in range(n):
            candidate = matrix[target_m][i]
            if candidate == target:
                return True
        return False

        