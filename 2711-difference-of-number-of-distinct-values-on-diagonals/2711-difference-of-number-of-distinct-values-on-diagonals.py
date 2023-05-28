class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        res = [[0] * m for _ in range(n)]
        def topLeft(i, j):
            unique = set()
            while(i > -1 and j > -1):
                unique.add(grid[i][j])
                i -= 1
                j -= 1
            return len(unique)
        def bottomRight(i, j):
            unique = set()
            while(i < n and j < m):
                unique.add(grid[i][j])
                i += 1
                j += 1
            return len(unique)
        for i in range(n):
            for j in range(m):
                res[i][j] = abs(topLeft(i - 1, j - 1) - bottomRight(i + 1, j + 1))
        return res

        