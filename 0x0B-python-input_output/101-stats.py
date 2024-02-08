#!/usr/bin/python3
"""Reads stdin line by line and computes metrics

Input format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
    prints those statistics since the beginning
"""


def print_statistics(size, status_code):
    """Prints statistics from the beginning
    Args:
        size (int): Accumulated read file size
        status_code (dict): Accumulated count of status codes
    """
    print("File size:  {}".format(size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_statistics(size, status_code)
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

        print_statistics(size, status_code)

    except KeyboardInterrupt:
        print_statistics(size, status_code)
        raise
