class Calculator:
    def __init__(self) -> None:
        self.result = 0

    def add(self, b):
        self.result += b

    def diff(self,b):
        self.result -= b