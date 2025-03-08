class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_nums = set(range(1, n*n + 1))
        repeated = None
        
        for row in grid:
            for num in row:
                if num in expected_nums:
                    expected_nums.remove(num)
                else:
                    repeated = num
        
        missing = next(iter(expected_nums))
        
        return [repeated, missing]