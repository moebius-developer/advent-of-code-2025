#!/usr/bin/env python

from pathlib import Path
import sys
import math

class Solution():
    def __init__(self):
        this_dir = Path(__file__).resolve().parent
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        else:
            input_file = this_dir.joinpath('input')

        answer = 0
        with open(input_file, 'r', encoding='utf-8') as file:
            for line in file:
                # maxx = -math.inf
                # maxn = -math.inf

                # second_maxn = 0
                # second_maxx = 0
                # for ix, chr in enumerate(line.strip()):
                #     num = int(chr)

                #     if num >= maxn:
                #         second_maxn = maxn
                #         second_maxx = maxx

                #         maxn = num
                #         maxx = ix
                #     elif num >= second_maxn:
                #         second_maxn = num
                #         second_maxx = ix

                # if second_maxx > maxx:
                #     batt = int(''.join([str(maxn), str(second_maxn)]))
                # elif maxx > second_maxx:
                #     batt = int(''.join([str(second_maxn), str(maxn)]))
                # else:
                #     raise RuntimeError('WTF?')

                # print(maxx, maxn, second_maxx, second_maxn, batt)

                stripped = line.strip()
                ix_of_biggest_number, biggest_number = self.find_biggest(stripped)

                first_number = None
                second_number = None
                len_stripped = len(stripped)
                if ix_of_biggest_number == (len_stripped - 1):
                    second_segment = stripped[0:-1]
                    second_number = biggest_number
                else:
                    second_segment = stripped[ix_of_biggest_number + 1:len_stripped]
                    first_number = biggest_number

                _, biggest_number = self.find_biggest(second_segment)

                if not first_number:
                    first_number = biggest_number
                elif not second_number:
                    second_number = biggest_number
                else:
                    raise RuntimeError('WTF?')

                answer += int(''.join([str(first_number), str(second_number)]))

        print(f"Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {answer}")

    def find_biggest(self, line: str) -> tuple[int, int]:
        maxx = -math.inf
        maxn = -math.inf

        for ix, chr in enumerate(line):
            num = int(chr)

            if num > maxn:
                maxn = num
                maxx = ix

        return int(maxx), int(maxn)

Solution()
