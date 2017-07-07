#!/usr/bin/env python3
# repair bar number issues in lilypond files

import os, sys, shutil, re

def read_file(file_name):
    # move to file writing section
    shutil.copy2(file_name, file_name + '.bak')

    with open(file_name) as f:
        read_lines = f.readlines()

    return read_lines

def increment_bar_number(line, increment):
    regex_num = re.compile(r"\s%\s\d+")
    regex_check = re.compile(r"\s#\d+")
    num = regex_num.search(line)
    check = regex_check.search(line)
    if num:
        print(num.group(), 'incremented by {}'.format(increment), end=' ')
        n = int(re.search(r"\d+", num.group()).group())
        n = n + increment
        print('is % {}'.format(n))
    elif check:
        print(check.group(), 'incremented by {}'.format(increment), end=' ')
        n = int(re.search(r"\d+", check.group()).group())
        n = n + increment
        print('is {}'.format(n))
    


def main():
    testfile = 'testfile.ly'
    data = read_file(testfile)
    
    for line in data:
        increment_bar_number(line, 1)

    # print(data)
    # for line in data:
        # print(line, end='')



if __name__ == "__main__":
    main()
