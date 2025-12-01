import sys
import re
sys.path.insert(0, "../2025")

from libs.puzzleInput import PuzzleInput
from FindPassword import FindPassword

puzzle = PuzzleInput('/home/jeff/Documents/projects/adventOfCode/2025/day1/puzzle.txt')
# print(puzzle.content)

findpassword = FindPassword(puzzle.content)
print(findpassword.calculatePassword())