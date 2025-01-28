class amir:
    def _init(self):
        self.string = ""
    def getString(self):
        self.string = input("Введите строку:")
    def printString(self):
        print(self.string.upper())

damir = amir()
damir.getString()
damir.printString()