#!/usr/bin/python3
"""Reads stdin line by line and computes metrics

Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
    prints those statistics since the beginning
"""

if __name__ == "__main__":
    import sys

    stdin = sys.stdin

    size = 0
    status_code = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in stdin:
            if count == 10:
                print("File size: {}".format(size))
                for key in sorted(status_code):
                    print("{}: {}".format(key, status_code[key]))
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print("File size: {}".format(size))
        for key in sorted(status_code):
            print("{}: {}".format(key, status_code[key]))

    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for key in sorted(status_code):
            print("{}: {}".format(key, status_code[key]))
        raise
