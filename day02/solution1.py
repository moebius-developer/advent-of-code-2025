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
                    str_form = str(num)
                    str_len = len(str_form)

                    if str_len % 2 != 0:
                        continue

                    chunk_len = int(str_len / 2)
                    chunk1 = str_form[0:chunk_len]
                    chunk2 = str_form[chunk_len:str_len]

                    if chunk1 == chunk2:
                        invalid_ids_total += int(str_form)

        print(f"Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {invalid_ids_total}")

Solution()
