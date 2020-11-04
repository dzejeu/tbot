from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    _called: int = -1

    def shift(self, amount_x, amount_y):
        return Point(self.x + amount_x, self.y + amount_y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        return self

    def __next__(self):
        if self._called == -1:
            self._called = 0
            return self.x
        elif self._called == 0:
            self._called = 1
            return self.y
        else:
            raise StopIteration
