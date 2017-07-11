SYNOPSIS
########

**ly-bar-incr** [OPTIONS] FILE

DESCRIPTION
###########
Increment bar numbers in comments and bar number checks of a lilypond file.

Mandatory arguments:
********************
FILE                  specify input file

optional arguments:
*******************
-h, --help            show this help message and exit

-i INCREMENT_VALUE, --increment-value INCREMENT_VALUE 
                      Specify number to increment by. Defaults to 1.

-d, --decrement       Decrement instead of incrementing.

-f FIRST_LINE, --first-line FIRST_LINE
                      Specify first line (inclusive) to increment on.
                      Default to start of file.

-l LAST_LINE, --last-line LAST_LINE
                      Specify last line (inclusive) to increment on.
                      Defaults to end of file.

-n, --dry-run        
                      write restult to stdout without affecting input file

OVERVIEW
########
This small utility is designed to increment all the marked bar numbers in a
lilypond file, generally to correct an error or renumber after and added or
removed measure. It was developed for use with files output by musicxml2ly so
it looks for numbers in the ends of lines preceded by **%** (comment) or **#** (bar
number check) and increments those numbers by one. The file is read and
re-written in place, and the previous version is copied to a new file with
the extension '.bak'

Different increments can be specified with **-i** as well as decrementing instead
(**-d**). These options can be combined: **-d -i3** would subtract 3 from each
specified bar number.

For errors or changes only affecting part of a file, you can specify starting
(**-f**) and/or ending lines (**-l**) to be changed. 

To see what the final file will look like without writing it, run with **-n** for
a dry run.

It is possible that some numbers at the ends of lines will be matched and
therefore incremented (notes should never match). For an added security, a
blank comment can be added to the end of a line.
