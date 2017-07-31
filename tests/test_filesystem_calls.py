"""Test filesystem calls."""
import unittest
from unittest import mock
from ly_bar_incr import ly_bar_incr

@mock.patch('builtins.open', create=True)
@mock.patch('builtins.print')
class FilesystemCallTest(unittest.TestCase):
    """Tests for filesystem calls."""

    def test_read_file(self, mock_print, mock_open):
        """Test reading the file in."""
        mock_open.return_value = mock.MagicMock()
        ly_bar_incr.read_file('testfile1')
        mock_open.assert_called_once_with('testfile1', 'r')
        # grab the mock file
        thefile = mock_open.return_value.__enter__.return_value
        thefile.readlines.assert_any_call()
        # if the file can't be read the program should exit
        with self.assertRaises(SystemExit):
            mock_open.side_effect = FileNotFoundError
            ly_bar_incr.read_file('nofile')
            mock_print.assert_called_once_with(mock.ANY)
            mock_open.reset_mock()
            mock_open.side_effect = PermissionError
            ly_bar_incr.read_file('nofile')
            mock_print.assert_called_once_with(mock.ANY)

    @mock.patch('ly_bar_incr.ly_bar_incr.shutil.copy2')
    def test_write_file(self, mock_copy, mock_print, mock_open):
        """Test backing up the file and writing it."""
        mock_open.return_value = mock.MagicMock()
        ly_bar_incr.write_file('some random text', 'mytestfile')
        # assure the file was copied and opened
        mock_copy.assert_called_once_with('mytestfile', 'mytestfile.bak')
        mock_open.assert_called_once_with('mytestfile', 'w')
        # grab the mock file
        thefile = mock_open.return_value.__enter__.return_value
        thefile.write.assert_called_once_with('some random text')
        mock_print.assert_called_once_with(mock.ANY)
