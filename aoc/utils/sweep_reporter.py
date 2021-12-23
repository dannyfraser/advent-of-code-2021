class SweepReporter:

    def __init__(self, depths:list[int]=None):
        self.depths = depths

    def clean_input(self, input:list) -> list:
        strip_newline = lambda x: x.replace("\n", "")
        return list(map(int, map(strip_newline, input)))

    def count_increases(self, window:int=1):
        # count the number of value increases across a sized window
        increases = 0
        for i in range(window, len(self.depths)):
            if sum(self.depths[i - window - 1:i - 1]) < sum(self.depths[i - window:i]):
                increases += 1
        return increases