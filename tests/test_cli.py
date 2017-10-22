import pytest
import click
import os
from click.testing import CliRunner
from unittest import mock
from ly_bar_incr import cli


@mock.patch('ly_bar_incr.read_file')
@mock.patch('ly_bar_incr.assemble_file')
@mock.patch('ly_bar_incr.write_file')
@mock.patch('ly_bar_incr.validate_lines')
def test_basic(mock_validate_lines, mock_write_file, mock_assemble_file,
               mock_read_file, monkeypatch, tmpdir):
    def let_it_pass(*args):
        pass
    mock_assemble_file.return_value = 'some random text'
    mock_read_file.return_value = 'some other random text'
    tmpfile = os.path.join(tmpdir, 'testfile.ly')
    with open(tmpfile, 'w') as f:
        f.write('a test file')
    runner = CliRunner()
    result = runner.invoke(cli, [tmpfile])
    assert result.exit_code == 0
    mock_read_file.assert_called_once_with(tmpfile)
    mock_write_file.assert_called_once_with('some random text', tmpfile)
    mock_assemble_file.assert_called_once_with(
        'some other random text', 1, 1, float("inf"))

    result2 = runner.invoke(cli, ['-i', '4', '-d', '-f', '10',
                                  '-l', '20', '-n', tmpfile])
    assert result2.exit_code == 0
    assert 'some' in result2.output
    mock_assemble_file.assert_called_with('some other random text', -4,
                                          10, 20)
