class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
       # 計算行的出現次數
        row_counts = {}
        for row in grid:
            row_tuple = tuple(row)  # 將每行轉換為元組以便哈希
            row_counts[row_tuple] = row_counts.get(row_tuple, 0) + 1
        
        count = 0
        n = len(grid)
        # 檢查每一列是否在行中出現
        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))  # 建構列的元組
            count += row_counts.get(col_tuple, 0)  # 如果列在行中出現，則增加對應的次數
        
        return count