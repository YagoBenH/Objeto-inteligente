import random

class Max30100Simulated:
    def __init__(self):
        self.bpm = 75 

    def bpm_simulator(self):
        self.bpm = random.randint(60, 100)
        return self.bpm
