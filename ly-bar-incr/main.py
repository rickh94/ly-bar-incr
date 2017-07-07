#!/usr/bin/env python3
# repair bar number issues in lilypond files

import sys, shutil, re, argparse

def read_file(file_name):

    # read the input file into a list of lines
    with open(file_name) as f:
        read_lines = f.readlines()

    return read_lines

def increment_bar_number(line, increment):
    # find the bar number
    regex_num = re.compile(r"\s[#%]\s?\d+")
    num = regex_num.search(line)
    # if it's found, extract the number and increment it
    if num:
        n = int(re.search(r"\d+", num.group()).group())
        n = n + increment
    # otherwise spit the line back out as is
    else:
        return line
    # if it's a comment, return as a comment
    if re.search(r"%", num.group()):
        return line.replace(num.group(), ' % {}'.format(n))
    # if it's a check, return as a check number
    elif re.search(r"#", num.group()):
        return line.replace(num.group(), ' #{}'.format(n))
    # something bad has occurred (hope not)
    else:
        print("Something has gone wrong")
        sys.exit(1)

def assemble_file(lines, inc, first_line, last_line):
    new_file = []
    i = 0
    for idx, line in enumerate(lines):
        # add just for indexing vs line numbers
        line_num = idx + 1

        # only increment within specified lines
        if line_num >= first_line and line_num <= last_line:
            new_line = increment_bar_number(line, inc)
        # otherwise spit the original line back out
        else:
            new_line = line

        new_file.append(new_line)

    # join it back into a stream and return it
    new_file_stream = ''.join(new_file)
    return new_file_stream

def write_file(file_stream, file_name):
    # backup the original file
    shutil.copy2(file_name, file_name + '.bak')
    # write the new data to the file
    with open(file_name, "w") as f:
        f.write(file_stream)

    print("{} has been written. Original is available at {}.bak".format(file_name, file_name))


def main():
    # hardcoded testfile
    # testfile = 'testfile.ly'

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


if __name__ == "__main__":
    main()
