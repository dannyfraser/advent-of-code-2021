class SubCommander:

    def __init__(self, command_string, command_type="basic"):
        self.commands = self._process_commands(command_string)
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def _process_commands(self, command_string):
        commands = []
        for com in command_string:
            direction, size = com.split(" ")
            size =int(size)
            commands.append({"direction":direction, "size":size})
        return commands

    def execute_commands_basic(self):
        self.horizontal = 0
        self.depth = 0
        for com in self.commands:
            if com["direction"] == "forward":
                self.horizontal += com["size"]
            if com["direction"] == "up": 
                self.depth -= com["size"]
            if com["direction"] == "down": 
                self.depth += com["size"]

    def execute_commands_advanced(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        for com in self.commands:
            if com["direction"] == "down":
                self.aim += com["size"]
            if com["direction"] == "up":
                self.aim -= com["size"]
            if com["direction"] == "forward":
                self.horizontal += com["size"]
                self.depth += (self.aim * com["size"])