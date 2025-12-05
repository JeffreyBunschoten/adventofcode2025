import sys
import re
sys.path.insert(0, "../2025")

from libs.puzzleInput import PuzzleInput
from MaxJoltage import MaxJoltage

puzzle = PuzzleInput('/home/jeff/Documents/projects/adventOfCode/2025/day3/puzzle.txt')
# print(puzzle.content)

output = MaxJoltage(puzzle.content)

# Solve puzzle with x amount of banks
# print(output.solve(2))
print(output.solve(12))
