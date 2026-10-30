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

        cur_pos = 50

        dir_map = {
            'L': -1,
            'R': 1
        }

        zero_count = 0

        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                direction = line[0]
                magni = int(line[1:])

                if magni > 100:
                    magni %= 100

                cur_pos += (dir_map[direction] * magni)

                if cur_pos < 0:
                    cur_pos += 100

                if cur_pos > 100:
                    cur_pos -= 100

                if cur_pos == 100:
                    cur_pos = 0

                if cur_pos == 0:
                    zero_count += 1


        print(f"Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {str(zero_count)}")

Solution()
