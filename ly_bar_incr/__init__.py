#!/usr/bin/env python3
import ly_bar_incr, sys, shutil, re, argparse

def main():

    # retrieve command line arguments
    parser = argparse.ArgumentParser(prog='ly-bar-incr',
            description='Increment bar numbers in comments and bar number checks of a lilypond file.'
            )

    # command line arguments
    parser.add_argument("FILE", help="specify input file")

    parser.add_argument("-i", "--increment-value", 
            type=int, default=1, 
            help="Specify number to increment by. Defaults to 1."
            )

    parser.add_argument("-d", "--decrement",
            action='store_true',
            help="Decrement instead of incrementing."
            )

    parser.add_argument("-f", "--first-line", 
            type=int, default=1,
            help="Specify first line (inclusive) to increment on. Default to start of file."
            )

    parser.add_argument("-l", "--last-line",
            type=int, default=float("inf"),
            help="Specify last line (inclusive) to increment on. Defaults to end of file."
            )

    parser.add_argument("-n", "--dry-run", 
            help="write restult to stdout without affecting input file",
            action="store_true"
            )

    args = parser.parse_args()
    
    # move args to variables
    in_file = args.FILE
    increment = args.increment_value

    # if decrement has been specified, make the increment value negative
    if args.decrement: increment = -increment

    data = read_file(in_file)
    out_file_stream = assemble_file(data, increment, args.first_line, args.last_line)

    # debug printing. may leave in for previewing
    if args.dry_run:
        print(out_file_stream)
    else:
        write_file(out_file_stream, in_file)
