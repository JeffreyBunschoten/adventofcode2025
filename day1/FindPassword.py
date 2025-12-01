import re

class FindPassword:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self._dialPointer = 50
        self._password = 0

    def _calculateDialPointer(self, direction, count):
        print(f"Received input:")
        if direction == "L":        
            self._dialPointer = (self._dialPointer - count) % 100
            print(f"Turning the knob Left {count} times\nPosition at: {self._dialPointer}\n")
        elif direction == "R":
            self._dialPointer = (self._dialPointer + count) % 100
            print(f"Turning the knob Right {count} times\nPosition at: {self._dialPointer}\n")
        else: 
            raise ValueError("direction must be either L or R")

    def split_input(self, line):
        match = re.match(r"([RL])(\d+)$", line)
        direction, count = match.groups()
        return direction, int(count)
    
    def calculatePassword(self):
        for line in self.puzzle:
            direction, count = self.split_input(line)
            self._calculateDialPointer(direction, count)
            if self._dialPointer == 0:
                self._password += 1
        return f"The secret Password is: {self._password}"
    