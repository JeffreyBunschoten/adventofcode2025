import sys
import re
sys.path.insert(0, "../2025")

from libs.puzzleInput import PuzzleInput
from MaxJoltage import MaxJoltage

puzzle = PuzzleInput('/home/jeff/Documents/projects/adventOfCode/2025/day3/puzzle.txt')
# print(puzzle.content)

output = MaxJoltage(puzzle.content)
maxJoltage = output.findMaxJoltage()
print(maxJoltage)