from animal import Animal

class Dog(Animal):
    def __init__(self) -> None:
        super().setName("개")
        super().setSound("멍멍")
        self.master = True
        pass

    # def printSound(self):
    #     print("멍멍")