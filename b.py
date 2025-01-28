class amir:
    def __init__(self):
        pass
    def area(self):
        print("Площадь формы: 0")        

class damir(amir):
    def __init__(self,length):
        self.length = length

    def area(self):
        self.area = self.length * self.length
        print(f"Площадь равна: {self.area}")

amir = amir()
amir.area()

length =  int(input("Выведите длину: "))
samir = damir(length)
samir.area()

