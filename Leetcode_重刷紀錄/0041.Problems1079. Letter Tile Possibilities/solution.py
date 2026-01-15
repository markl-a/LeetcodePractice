"""
1079. Letter Tile Possibilities

Difficulty: Medium
Topics: Hash Table, String, Backtracking, Counting

Problem:
    [Problem description goes here]

Example 1:
    Input: ...
    Output: ...

Constraints:
    - ...
"""

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = {}
        for tile in tiles:
            counts[tile] = counts.get(tile, 0) + 1

        unique_sequences = set()

        def backtrack(current_sequence):
            if current_sequence:
                unique_sequences.add(current_sequence)

            for tile, count in counts.items():
                if count > 0:
                    counts[tile] -= 1
                    backtrack(current_sequence + tile)
                    counts[tile] += 1

        backtrack("")
        return len(unique_sequences)
