class Position:
    def __init__(self, row:int, column:int) -> None:
        self.row = row
        self.column = column

    @classmethod
    def from_tuple(cls, coords:tuple[int]):
        return cls(coords[0], coords[1])