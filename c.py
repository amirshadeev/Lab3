class Rectangle:
    def __init__(self):
        pass
    def area(self):
        print("Площадь формы:0 ")
    
class amir(Rectangle):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        self.area = self.length * self.width
        print(f"Площадь равнa: {self.area}")

damir = Rectangle()
damir.area()

length = int(input("Выведите длину:"))
width = int(input("Выведите ширину:"))
samir = amir(length,width)
samir.area()