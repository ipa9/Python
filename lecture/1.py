class Figure():
    side = 5
    def area(self):
        return self.side**2

square = Figure()
print(square.side)
print(square.area())
