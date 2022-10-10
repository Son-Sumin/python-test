from human import Human


class Arm(Human) :
    def __init__(self,side,name) -> None:
        print("팔")
        self.side = side
        super().setName(name)
        pass