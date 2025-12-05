import pandas as pd

class AccessiblePaper():
    def __init__(self, puzzle: list, reachable: int):
        self.grid = pd.DataFrame([list(row) for row in puzzle])
        self.reachable = reachable
        self.accessible = []
        self.rows = self._calculate_rows()
        self.columns = self._calculate_columns()

    def map_locations(self):
        pass

    def _calculate_rows(self):
        return len(self.grid)

    def _calculate_columns(self):
        return len(self.grid.columns)