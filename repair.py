#!/usr/bin/env python3
# repair bar number issues in lilypond files

import sys, shutil, re

def read_file(file_name):
    # move to file writing section
    shutil.copy2(file_name, file_name + '.bak')

    with open(file_name) as f:
        read_lines = f.readlines()

    return read_lines

def increment_bar_number(line, increment):
    regex_num = re.compile(r"\s[#%]\s?\d+")
    num = regex_num.search(line)
    if num:
        n = int(re.search(r"\d+", num.group()).group())
        n = n + increment
    else:
        return line
    if re.search(r"%", num.group()):
        return line.replace(num.group(), ' % {}'.format(n))
    elif re.search(r"#", num.group()):
        return line.replace(num.group(), ' #{}'.format(n))
    else:
        print("Something has gone wrong")
        sys.exit(1)

def assemble_file(lines, inc, first_line=1, last_line=float("inf")):
    new_file = []
    i = 0
    for idx, line in lines:
        # add just for indexing vs line numbers
        line_num = idx + 1

        # only increment within specified lines
        if line_num >= first_line and line_num <= last_line:
            new_line = increment_bar_number(line, inc)
        # otherwise spit the original line back out
        else:
            new_line = line

        new_file.append(new_line)

    new_file_stream = ''.join(new_file)
    return new_file_stream

def main():
    testfile = 'testfile.ly'
    data = read_file(testfile)

    out_file_stream = assemble_file(data, 1)
    print(out_file_stream)


if __name__ == "__main__":
    main()
