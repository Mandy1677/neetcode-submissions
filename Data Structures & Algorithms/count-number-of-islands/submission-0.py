class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[0,1], [-1,0],[0,-1]]
        rowCount, colCount = len(grid), len(grid[0])
        ans = 0
        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = dr + row, dc + col
                    if (newr < 0 or newc < 0 or newr >= rowCount 
                    or newc >= colCount or grid[newr][newc] == "0"):
                      continue
                    q.append((newr, newc))
                    grid[newr][newc] = "0"
        for r in range(rowCount):
            for c in range(colCount):
                if grid[r][c] == "1":
                    bfs(r, c)
                    ans += 1
        return ans





        