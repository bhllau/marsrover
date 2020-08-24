"""Solution to Mars Rover Problem in Python 3.7.

Date: 23/08/2020
Author: Bruce Lau
Email: hllau@hllau.com
"""
from typing import Tuple, Optional
import sys


# define cardinal directions
CARDINALS = 'NESW'

# define plateau type as a 2D size
# (it is a stub; the example input/output does not need plateau size)
Plateau = Tuple[int, int]


class Rover():
    """Return a rover object with properties 1) position (x, y) and 2) a
    direction which is 'N', 'E', 'S' or 'W', which can move when provided
    with instructions (see method "move")."""

    def __init__(
            self,
            plateau: Plateau,
            x: int,
            y: int,
            direction: str,
            ops: Optional[str]=None,
            ):
        self.plateau = plateau
        self.x = x
        self.y = y
        self.direction = direction
        self.move(ops)

    @property
    def direction(self) -> str:
        """Convert the internal integer representation of direction to
        string."""
        return CARDINALS[self._direction]

    @direction.setter
    def direction(self, value: str) -> None:
        """Coerce direction from string to integer internally for easier
        handling."""
        self._direction = CARDINALS.index(value)

    def __move(self, op: str) -> None:
        """Move on a single operation."""
        if op == 'R':
            # spin 90 degree right
            self._direction = (self._direction + 1) % 4

        elif op == 'L':
            # spin 90 degree left
            self._direction = (self._direction - 1) % 4

        elif op == 'M':
            # move 1 step forward, avoid crossing boundary for safely
            # (don't fall off from the suspicious rectangular mars!)
            (max_x, max_y) = self.plateau
            if self._direction == 0:
                self.y = min(max_y, self.y + 1)
            elif self._direction == 1:
                self.x = min(max_x, self.x + 1)
            elif self._direction == 2:
                self.y = max(0, self.y - 1)
            elif self._direction == 3:
                self.x = max(0, self.x - 1)

        else:
            raise ValueError('Operation must be one of "L", "R" or "M"!')

    def move(self, ops: Optional[str]=None) -> None:
        """Move rover according to input operations. Operations can be a
        string containing 'L', 'R' or 'M'.

        - 'L' will rotate rover 90 degree to the left (i.e. from facing
          north to west).
        - 'R' will rotate rover 90 degree to the right
          (i.e. from facing north to east).
        - 'M' will move rover forward
          one grid point, maintaining the same heading (i.e. 0 0 N -> 0 1 N).
        """
        # handle multiple movements in a single string
        if ops is not None:
            for op in ops:
                self.__move(op)

    def __str__(self) -> str:
        """A string representation of the location and heading of the rover."""
        return f"{self.x} {self.y} {self.direction}"


def get_rover(plateau: Plateau, line: str) -> Rover:
    """Return the final location of an input rover plus operations.

    >>> f"{get_rover((5, 5), '0 0 N M')}"
    '0 1 N'
    >>> f"{get_rover((2, 2), '1 1 E RM')}"
    '1 0 S'
    """
    (x, y, direction, ops) = line.rstrip().split()
    rover = Rover(plateau, int(x), int(y), direction, ops)
    return rover


def play(input_stream, output_stream) -> None:
    """Read rover moves from input_stream and output them line by line.

    First line indicates the size of the plateau. Subsequent lines
    describe the location, the cardinal direction of the rover and
    the moves to take from the NASA instructions. See unit tests for
    sample inputs and outputs.
    """
    plateau: Optional[Plateau] = None
    for input_line in input_stream:
        if plateau is None:
            # first line: obtain size of plateau (coerse input to int)
            xstr, ystr = input_line.rstrip().split()
            plateau = int(xstr), int(ystr)
            continue
        # for all other lines: process them one by one
        print(get_rover(plateau, input_line), file=output_stream)


if __name__ == '__main__':
    play(sys.stdin, sys.stdout)

