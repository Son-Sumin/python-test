from human import Human


class Leg(Human):
    def __init__(self,side,name) -> None:
        print("다리")
        self.side = side
        super().setName(name)
        pass