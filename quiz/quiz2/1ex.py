#1. Write a class called lists. The class must have a constructor with the parameter as a list and it prints it on the screen. 
#The class has a method that counts the sum of the numbers in this list and the minimum and maximum values of it. 
#Create a class object and pass it some list. The sum of the elements of this list, the minimum and maximum number must be printed to the screen.

class Lists:
    def __init__(self, _list):
        self._list = _list
        print(self._list)

    def __str__(self):
        return "min: " + str(min(self._list)) + "\n" + \
                "max: " + str(max(self._list)) + "\n" + \
                "sum: " + str(sum(self._list))

example = (10, 20, 30, 40)
list = Lists(example)
print(list)
