#!/usr/bin/env python

from pathlib import Path
import sys

class Solution():
    def __init__(self):
        this_dir = Path(__file__).resolve().parent
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        else:
            input_file = this_dir.joinpath('input')

        invalid_ids_total = 0
        with open(input_file, 'r', encoding='utf-8') as file:
            ranges = [item.strip() for item in file.read().split(',')]

            for span in ranges:
                start, end = [int(item.strip()) for item in span.split('-')]

                for num in range(start, end + 1):
                    if self.has_repeated_pattern(str(num)):
                        invalid_ids_total += num

        print(f"Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {invalid_ids_total}")

    def has_repeated_pattern(self, s: str) -> bool:
        if not s:
            return False

        return s in (s + s)[1:-1]

Solution()
