#!/usr/bin/env python

from pathlib import Path
import sys
import heapq

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
                nums = [int(nstr) for nstr in line.strip()]
                batt = self.max_number_preserving_order(nums, 12)
                answer += int(batt)

        print(f'Day {str(this_dir)[-1]}, part {Path(__file__).stem[-1]}: {answer}')

    def max_number_preserving_order(self, nums: list[int], k: int) -> str:
        drop = len(nums) - k
        stack = []

        for num in nums:
            while drop > 0 and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)

        result = stack[:k]

        return ''.join(map(str, result))

Solution()
