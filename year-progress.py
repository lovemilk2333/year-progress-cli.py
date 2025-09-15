#!/usr/bin/env python3

import sys
import argparse
from datetime import datetime

VERSION = (1, 0)

parser = argparse.ArgumentParser(
    prog="year-progress.py", description="Display how many days you lost this year", allow_abbrev=False
)
parser.add_argument("--version", "-v", action="store_true",
                    help="Display version info")
parser.add_argument("--width", type=int, help="The progress bar width")
args = parser.parse_args()

if args.version:
    print(f'v2.0-{VERSION[0]}.{VERSION[1]}')
    sys.exit()

if args.width is not None:
    print_width = args.width
    if print_width < 3:
        print("Error: Width < 3")
        exit(1)
else:
    print_width = int(0.6 * 80)

now = datetime.now()
tm_yday = int(now.strftime('%j'))
current_year = now.year
days_year = (
    datetime(current_year + 1, 1, 1) -
    datetime(current_year, 1, 1)
).days

year_ratio = tm_yday / days_year
year_percent = year_ratio * 100

print(
    "It's day ",
    tm_yday,
    " of the year(",
    days_year,
    "). That's already ",
    format(year_percent, ".1f"),
    "%",
    sep="",
)

print("[", end="")

for i in range(print_width - 2):
    if i <= print_width * year_ratio:
        print("-", end="")
    else:
        print("#", end="")

print("]", end="\n")
