class MaxJoltage:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def findMaxJoltage(self, digits, picks):
        """
        Choose `picks` digits from `digits` (string of digits), preserving order,
        that form the lexicographically largest possible number.
        """
        digits = list(map(int, digits))
        n = len(digits)
        chosen = []
        start = 0

        for _ in range(picks):
            remaining_picks = picks - len(chosen)
            max_index = n - remaining_picks

            best_digit = -1
            best_pos = -1
            for i in range(start, max_index + 1):
                if digits[i] > best_digit:
                    best_digit = digits[i]
                    best_pos = i

            chosen.append(best_digit)
            start = best_pos + 1 # Next digit to pick to the right always

        return int("".join(map(str, chosen)))
    
    def solve(self, picks):
        total = 0
        for line in self.puzzle:
            total += self.findMaxJoltage(line.strip(), picks)
        return total
    