from aoc.utils.sub_commander import SubCommander

commands = [
    "forward 5",
    "down 5",
    "forward 8",
    "up 3",
    "down 8",
    "forward 2"
]
commander = SubCommander(commands)

def test_part_1():
    commander.execute_commands_basic()
    commander.horizontal * commander.depth == 150

def test_part_2():
    commander.execute_commands_advanced()
    commander.horizontal * commander.depth == 900