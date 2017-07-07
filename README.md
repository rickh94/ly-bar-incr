# ly-bar-incr
Simple script to increment bar numbers in comments and number checks in lilypond files.

## Usage
usage: ly-bar-incr [-h] [-i INCREMENT_VALUE] [-d] [-f FIRST_LINE]
                   [-l LAST_LINE] [-n]
                   FILE

Increment bar numbers in comments and bar number checks of a lilypond file.

| Argument | Description |
|----------|-------------|
| FILE     | __REQUIRED__ : specify input file |
|-h, --help | show this help message and exit |
|-i INCREMENT_VALUE --increment-value INCREMENT_VALUE| Specify number to increment by. Defaults to 1.|
|-d, --decrement | Decrement instead of incrementing. |
|-f FIRST_LINE, --first-line FIRST_LINE | | Specify first line (inclusive) to increment on. Default to start of file.|
|-l LAST_LINE, --last-line LAST_LINE | Specify last line (inclusive) to increment on. Defaults to end of file.|
|-n, --dry-run | write restult to stdout without affecting input file |
