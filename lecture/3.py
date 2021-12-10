class Figure():
    def __init__(self,x):
        self.x=x
        print("I am created and I am the " + str(self.x))
    def area(self,side):
        self.side = side
        return self.side**2
    def info(self):
        return "the side is " + str(self.side)

square = Figure("square")
