class MaxJoltage:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def findMaxJoltage(self):
        total_joltage = 0
        for battery in self.puzzle:
            digits = [int(digit) for digit in battery]
            
            # Find the two largest digits
            largest_digit = max(digits)
            index_largest = digits.index(largest_digit) # Keep the indexcount for startposition secondnumber
            digits.remove(largest_digit)
            
            # From left to right scanning
            try:
                second_largest_digit = max(digits[index_largest:])  # Find the second largest digit
                joltage = int(f"{largest_digit}{second_largest_digit}")
                total_joltage += joltage

            # Flip the list around if the largest N is at the end (from R to L)
            except ValueError as err:
                second_largest_digit = max(digits[-index_largest:])
                joltage = int(f"{second_largest_digit}{largest_digit}")
                total_joltage += joltage
        
        return total_joltage
    