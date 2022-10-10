class APerson :
    count = 0
    def __init__(self) -> None:
        APerson.count +=1
        self.count += 1

    @classmethod
    def printCount(cls):  #cls = Person
        print(cls.count)

    def printCount2(self):  #self = c
        print(self.count)