"""Tests validation of line numbers."""
import pytest
from ly_bar_incr import validate_lines


def test_validate_lines():
    """Test validation of specified line numbers."""
    # this should do nothing
    validate_lines(fline=1, lline=2, total=3)
    validate_lines(fline=1, lline=float("inf"), total=20)

    arr = [n for n in range(1, 101)]
    validate_lines(fline=1, lline=100, total=len(arr))

    with pytest.raises(SystemExit):
        validate_lines(fline=100, lline=101, total=30)

    with pytest.raises(SystemExit):
        validate_lines(fline=20, lline=10, total=40)

    with pytest.raises(SystemExit):
        validate_lines(fline=-1, lline=10, total=20)

    with pytest.raises(SystemExit):
        validate_lines(fline=1, lline=-5, total=20)
