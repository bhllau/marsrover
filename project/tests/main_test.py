"""Unit tests for mars rover problem."""
import unittest
import io

from project.main import Rover, play


class TestRover(unittest.TestCase):
    """Unit tests for rover's moves."""

    def test_spin_r_from_n(self):
        """Spin right facing north."""
        rover = Rover((5, 5), 2, 2, 'N', 'R')
        self.assertEqual(f'{rover}', '2 2 E')

    def test_spin_l_from_n(self):
        """Spin left facing north."""
        rover = Rover((5, 5), 2, 2, 'N', 'L')
        self.assertEqual(f'{rover}', '2 2 W')

    def test_spin_r_from_e(self):
        """Spin right facing east."""
        rover = Rover((5, 5), 2, 2, 'E', 'R')
        self.assertEqual(f'{rover}', '2 2 S')

    def test_spin_l_from_e(self):
        """Spin left facing east."""
        rover = Rover((5, 5), 2, 2, 'E', 'L')
        self.assertEqual(f'{rover}', '2 2 N')

    def test_spin_r_from_s(self):
        """Spin right facing south."""
        rover = Rover((5, 5), 2, 2, 'S', 'R')
        self.assertEqual(f'{rover}', '2 2 W')

    def test_spin_l_from_s(self):
        """Spin left facing south."""
        rover = Rover((5, 5), 2, 2, 'S', 'L')
        self.assertEqual(f'{rover}', '2 2 E')

    def test_spin_r_from_w(self):
        """Spin right facing west."""
        rover = Rover((5, 5), 2, 2, 'W', 'R')
        self.assertEqual(f'{rover}', '2 2 N')

    def test_spin_l_from_w(self):
        """Spin left facing west."""
        rover = Rover((5, 5), 2, 2, 'W', 'L')
        self.assertEqual(f'{rover}', '2 2 S')

    def test_move_facing_n(self):
        """Move one step facing north."""
        rover = Rover((5, 5), 2, 2, 'N', 'M')
        self.assertEqual(f'{rover}', '2 3 N')

    def test_move_facing_e(self):
        """Move one step facing east."""
        rover = Rover((5, 5), 2, 2, 'E', 'M')
        self.assertEqual(f'{rover}', '3 2 E')

    def test_move_facing_s(self):
        """Move one step facing south."""
        rover = Rover((5, 5), 2, 2, 'S', 'M')
        self.assertEqual(f'{rover}', '2 1 S')

    def test_move_facing_w(self):
        """Move one step facing west."""
        rover = Rover((5, 5), 2, 2, 'W', 'M')
        self.assertEqual(f'{rover}', '1 2 W')


class TestGames(unittest.TestCase):
    """Integration tests for different setups.

    Since the size of plateau is provided, this will also test rover
    when they are located at the boundary of the rectangular plateau.
    """

    testsmap = {
            'example': ('''\
5 5
1 2 N LMLMLMLMM
3 3 E MMRMMRMRRM
''',
'''\
1 3 N
5 1 E
'''),

            'zero': ('0 0\n', ''),

            'no-further-input': ('1 1\n', ''),

            'add-extra-line': ('''\
10 10
1 2 N LMLMLMLMM
3 3 E MMRMMRMRRM
1 1 N LMLMLMLMMM
''',
'''\
1 3 N
5 1 E
1 3 N
'''),

            'out-of-border': ('''\
5 5
0 0 S M
0 0 W M
5 5 N M
5 5 E M
''',
'''\
0 0 S
0 0 W
5 5 N
5 5 E
'''),

    }

    def test_games(self):
        """Loop and test the defined maps above."""
        for name, (a, b) in self.testsmap.items():
            with self.subTest(name=name):
                input_, output = io.StringIO(a), io.StringIO()
                play(input_, output)
                self.assertEqual(output.getvalue(), b)

