class PuzzleInput:
    def __init__(self, filepath):
        self.filepath = filepath
        self.content = self._load_content()

    def _load_content(self):
        with open(self.filepath, 'r') as file:
            return [line.rstrip('\n') for line in file]

