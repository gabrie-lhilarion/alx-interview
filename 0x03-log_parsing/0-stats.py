#!/usr/bin/python3

import sys
import signal

total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


def print_stats():
    global total_file_size, status_code_counts
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, dash, date, method, path, protocol, status, size = parts

        notget = method != '"GET'
        nothttp1 = protocol != 'HTTP/1.1"'
        motstartwith = not path.startswith('/projects/260')

        if notget or nothttp1 or motstartwith:
            continue

        try:
            size = int(size)
            status = str(status)
        except ValueError:
            continue

        total_file_size += size

        if status in status_code_counts:
            status_code_counts[status] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}")

finally:
    print_stats()
