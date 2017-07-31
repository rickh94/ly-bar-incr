import unittest
from ly_bar_incr import ly_bar_incr

class IncrTest(unittest.TestCase):
    """Test incrementing function."""

    def setUp(self):
        self.test1 = 'a4 es g -. d | % 1'
        self.test2 = 'g8 c16 d e f gs | % 122'
        self.test3 = 'r8 g8 g g | e2'
        self.test4 = 'e8 f f f | \\barNumberCheck #4'
        self.test5 = 'd4 d8. d16 d4 d | % 100'
        self.test6 = '\\override font-size = #10'

    def test_increment_bar_number(self):
        """Test the incrementing of lines."""
        # basic
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test1, 1),
            'a4 es g -. d | % 2')
        # negative
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test2, -1),
            'g8 c16 d e f gs | % 121')
        # no bar number found
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test3, 1),
            'r8 g8 g g | e2')
        # number check
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test4, 1),
            'e8 f f f | \\barNumberCheck #5')
        # increment by more than 1
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test5, 11),
            'd4 d8. d16 d4 d | % 111')
        # don't increment non-checks
        self.assertEqual(
            ly_bar_incr.increment_bar_number(
                self.test6, 1),
            '\\override font-size = #10')
