import sys
import re
sys.path.insert(0, "../2025")

from libs.puzzleInput import PuzzleInput
from FindPassword import FindPassword

puzzle = PuzzleInput('/home/jeff/Documents/projects/adventOfCode/2025/day1/puzzle.txt')
# print(puzzle.content)

# The dial has N positions (N = 100)
# You start at position 50
# You rotate k steps (positive for right, negative for left)
# Formule Turning Left: passes = (start + k) // N
# Formule Turning Right: passes = ((N - 1 + start) - k) // N

findpassword = FindPassword(puzzle.content, method='0x434C49434B')
print(findpassword.calculatePassword())