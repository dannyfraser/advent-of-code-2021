from utils.file_readers import read_int_list
from utils.sweep_reporter import SweepReporter

def solve():
    depths = read_int_list("inputs/day_01.txt")
    reporter = SweepReporter(depths)

    count = reporter.count_increases()
    print(f"day 1 part 1 solution: {count}")

    count = reporter.count_increases(window=3)
    print(f"day 1 part 2 solution: {count}")

if __name__ == "__main__":
    solve()