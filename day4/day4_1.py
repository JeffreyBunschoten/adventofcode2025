import sys
import re
import pandas as pd
sys.path.insert(0, "../2025")

from libs.puzzleInput import PuzzleInput
from AccessiblePaper import AccessiblePaper

puzzle = PuzzleInput('/home/jeff/Documents/projects/adventOfCode/2025/day4/example_puzzle.txt')
# print(puzzle.content)

# Day4_1 reachable when less then 4 adjacent rolls
output = AccessiblePaper(puzzle.content, 4)
print(output.grid)

pickable_locations = []
for column, row in output.grid.iterrows():
    if row.index == 0:
        print("Top Row")