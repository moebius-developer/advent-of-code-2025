#!/usr/bin/env python

from pathlib import Path
import sys

class Solution():
    ROLL_CHAR = '@'
    def __init__(self):
        this_dir = Path(__file__).resolve().parent
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        else:
            input_file = this_dir.joinpath('input')

        answer = 0
        with open(input_file, 'r', encoding='utf-8') as file:
            grid = []
            for line in file:
                row = []
                for item in line.strip():
                    row.append(item)

                grid.append(row)

            self.grid = grid
            self.grid_len = len(self.grid)
            self.row_len = len(self.grid[0])

            for row_ix, row in enumerate(grid):
                for col_ix, item in enumerate(row):
                    if self.is_accessible(item, row_ix, col_ix):
                        answer += 1

        print(f"Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {answer}")

    def is_accessible(self, item: str, row_ix: int, col_ix: int) -> bool:
        if item != Solution.ROLL_CHAR:
            return False

        num_found = 0
        # Up, left
        if (row_ix - 1) >= 0 and (col_ix - 1) >= 0 and self.grid[row_ix - 1][col_ix - 1] == Solution.ROLL_CHAR:
            num_found += 1

        # Up, center
        if (row_ix - 1) >= 0 and self.grid[row_ix - 1][col_ix] == Solution.ROLL_CHAR:
            num_found += 1

        # Up, right
        if (row_ix - 1) >= 0 and (col_ix + 1) < self.row_len and self.grid[row_ix - 1][col_ix + 1] == Solution.ROLL_CHAR:
            num_found += 1

        # Right
        if (col_ix + 1) < self.row_len and self.grid[row_ix][col_ix + 1] == Solution.ROLL_CHAR:
            num_found += 1

        # Down, right
        if (row_ix + 1) < self.grid_len and (col_ix + 1) < self.row_len and self.grid[row_ix + 1][col_ix + 1] == Solution.ROLL_CHAR:
            num_found += 1

        # Down, center
        if (row_ix + 1) < self.grid_len and self.grid[row_ix + 1][col_ix] == Solution.ROLL_CHAR:
            num_found += 1

        # Down, left
        if (row_ix + 1) < self.grid_len and (col_ix - 1) >= 0 and self.grid[row_ix + 1][col_ix - 1] == Solution.ROLL_CHAR:
            num_found += 1

        # Left
        if (col_ix - 1) >= 0 and self.grid[row_ix][col_ix - 1] == Solution.ROLL_CHAR:
            num_found += 1

        if num_found > 3:
            return False

        return True

Solution()
