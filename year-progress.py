#!/usr/bin/env python3

import argparse
import time

parser = argparse.ArgumentParser(
    prog="year-progress.py", description="Display how many days you lost this year", allow_abbrev=False
)
parser.add_argument("--version", "-v", action="version", version="develop", help="Display version info")
parser.add_argument("--width", type=int, help="The progress bar width")
args = parser.parse_args()

if args.width != None:
    print_width = args.width
    if print_width < 3:
        print("Error: Width < 3")
        exit(1)
else:
    print_width = int(0.6 * 80)

tm = time.localtime()
if tm.tm_year % 4 == True:
    days_year = 366
else:
    days_year = 365

year_ratio = tm.tm_yday / days_year
year_percent = year_ratio * 100

print(
    "It's day ",
    tm.tm_yday,
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
