"""Repair bar number mistakes in lilypond files."""
import argparse
import os
import re
import shutil


def read_file(file_name):
    """Read the input file into a list of lines."""
    try:
        with open(file_name, 'r') as f:
            read_lines = f.readlines()
    except FileNotFoundError:
        print("File could not be found. Please try again.")
        raise SystemExit(1)
    except PermissionError:
        print("Could not open file (insufficient privileges).")
        raise SystemExit(1)

    return read_lines


def increment_bar_number(line, increment):
    """Increments a bar number (if found) on a line and returns the line."""
    # skip some stuff if it isn't relevant
    if '\\barNumberCheck #' not in line and '%' not in line:
        return line
    # this regex actually finds the numbers and makes groups
    regex_num = re.compile(r"\s([#%]\s?)(\d+)")
    num = regex_num.search(line)

    if num:
        n = int(num.group(2))
        n = n + increment
        line = line.replace(num.group(2), '{}'.format(n))

    # return line whether or not it has been touched
    return line


def assemble_file(lines, inc, first_line, last_line):
    """Assemble the file from incremented and non-incremented lines."""
    new_file = []
    for idx, line in enumerate(lines):
        # indicies start from zero, line numbers start from 1
        line_num = idx + 1

        # only increment within specified lines
        if line_num >= first_line and line_num <= last_line:
            new_line = increment_bar_number(line, inc)
        else:
            new_line = line

        new_file.append(new_line)

    new_file_stream = ''.join(new_file)
    return new_file_stream


def write_file(file_stream, file_name):
    """Backups up the old file and overwrites it in place.

    If it cannot write because of a permission error it writes a new file to
    /tmp and leaves the original untouched.
    """
    try:
        # backup the original file
        shutil.copy2(file_name, file_name + '.bak')
        path = file_name
        message = ("{} has been written. Original is available at "
                   "{}.bak").format(file_name, file_name)
    except PermissionError:
        base_name = os.path.basename(file_name)
        path = os.path.join('/tmp', base_name)
        message = ("Could not write {orig} (permission error). New file has "
                   "been written to {new}. Make sure that you have "
                   "write permission to {orig} for future runs.").format(
                       orig=file_name,
                       new=path)

    with open(path, "w") as f:
        f.write(file_stream)
    print(message)


def main():
    """Main function."""
    # retrieve command line arguments
    parser = argparse.ArgumentParser(
        prog='ly-bar-incr',
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
                        help=("Specify first line (inclusive) to increment "
                              "on. Default to start of file.")
                       )

    parser.add_argument("-l", "--last-line",
                        type=int, default=float("inf"),
                        help=("Specify last line (inclusive) to increment "
                              "on. Defaults to end of file.")
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
    if args.decrement:
        increment = -increment

    data = read_file(in_file)
    out_file_stream = assemble_file(data, increment, args.first_line, args.last_line)

    if args.dry_run:
        print(out_file_stream)
    else:
        write_file(out_file_stream, in_file)


if __name__ == "__main__":
    main()
