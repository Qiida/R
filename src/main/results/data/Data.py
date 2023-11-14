from abc import ABC


class Data(ABC):
    def __init__(self, time: int, value: float):
        self.t = time
        self.value = value
