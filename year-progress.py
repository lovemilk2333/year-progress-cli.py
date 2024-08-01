import argparse
import time

parser = argparse.ArgumentParser(
    prog="year-progress.py", description="Display how many days you lost this year", allow_abbrev=False
)
parser.add_argument("--version", "-v", action="version", version="develop", help="display version info")
parser.add_argument("--max-width", type=int, help="the progress bar width")
args = parser.parse_args()

if args.max_width != None:
    print_width = args.max_width
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
    "This year has lost ",
    tm.tm_yday,
    "/",
    days_year,
    " days. That's already ",
    format(year_percent, ".3f"),
    "%",
    sep="",
)

if print_width <= 3:
    print("Error: Width <= 3")
    exit(1)

print("[", end="")

for i in range(print_width - 2):
    if i <= print_width * year_ratio:
        print("-", end="")
    else:
        print("#", end="")

print("]", end="\n")
