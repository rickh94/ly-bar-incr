"""Tests the assemble file function."""
import unittest
from unittest import mock
from ly_bar_incr import ly_bar_incr

class AssembleFileTest(unittest.TestCase):
    """Test assembling file."""

    def setUp(self):
        self.list_of_lines = [
            'this is a line\n',
            'this is a line\n',
            'this is a line\n',
            'this is a line\n',
            'this is a line\n',
            'this is a line\n'
            ]
        self.joined_lines = (
            'this is a line\nthis is a line\n'
            + 'this is a line\nthis is a line\nthis is a line\n'
            + 'this is a line\n')

    @mock.patch('ly_bar_incr.ly_bar_incr.increment_bar_number')
    def test_assemble_file(self, mock_incr):
        """Test assemble file."""
        # test with default values
        mock_incr.return_value = 'this is a line\n'
        self.assertEqual(
            ly_bar_incr.assemble_file(
                self.list_of_lines, 1, 1, float("inf")),
            self.joined_lines)
        mock_incr.assert_any_call('this is a line\n', 1)
        mock_incr.mock_reset()

        # test specified last line
        mock_incr.assert_any_call('this is a line\n', 1)
        mock_incr.return_value = 'this is a different line\n'
        self.assertEqual(
            ly_bar_incr.assemble_file(
                self.list_of_lines, 1, 1, 3),
            ('this is a different line\nthis is a different line\n'
             + 'this is a different line\nthis is a line\n'
             + 'this is a line\nthis is a line\n'))
        mock_incr.assert_any_call('this is a line\n', 1)
        mock_incr.mock_reset()

        # test specified first line
        mock_incr.return_value = 'this is a different line\n'
        self.assertEqual(
            ly_bar_incr.assemble_file(
                self.list_of_lines, 1, 5, float("inf")),
            ('this is a line\nthis is a line\n'
             + 'this is a line\nthis is a line\n'
             + 'this is a different line\nthis is a different line\n'))
        mock_incr.assert_any_call('this is a line\n', 1)
        mock_incr.mock_reset()

        # test both
        mock_incr.return_value = 'this is a different line\n'
        self.assertEqual(
            ly_bar_incr.assemble_file(
                self.list_of_lines, 1, 4, 5),
            ('this is a line\nthis is a line\n'
             + 'this is a line\nthis is a different line\n'
             + 'this is a different line\nthis is a line\n'))
        mock_incr.assert_any_call('this is a line\n', 1)
        mock_incr.mock_reset()

        # test different increment value
        mock_incr.return_value = 'this is a line\n'
        self.assertEqual(
            ly_bar_incr.assemble_file(
                self.list_of_lines, 6, 1, float("inf")),
            ('this is a line\nthis is a line\n'
             + 'this is a line\nthis is a line\n'
             + 'this is a line\nthis is a line\n'))
        mock_incr.assert_any_call('this is a line\n', 6)
        mock_incr.mock_reset()
