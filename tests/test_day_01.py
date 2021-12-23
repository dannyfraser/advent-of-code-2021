from aoc.utils.sweep_reporter import SweepReporter

test_input =[199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
reporter = SweepReporter(depths=test_input)

def test_part_1():
    reporter.count_increases() == 7

def test_part_2():
    reporter.count_increases(window=3) == 5