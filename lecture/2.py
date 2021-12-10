class Figure():
    def area(self,side):
        self.side = side
        return self.side**2
    def info(self):
        return "the side is " + str(self.side)

square = Figure()
print(square.area(5))
print(square.info())
