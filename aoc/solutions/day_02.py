from utils.file_readers import read_generic_text
from utils.sub_commander import SubCommander

def solve():
    commands = read_generic_text("inputs/day_02.txt")
    commander = SubCommander(commands)

    commander.execute_commands_basic()
    result = commander.depth * commander.horizontal
    print(f"day 2 part 1 solution: {result}")

    commander.execute_commands_advanced()
    result = commander.depth * commander.horizontal
    print(f"day 2 part 2 solution: {result}")

if __name__ == "__main__":
    solve()