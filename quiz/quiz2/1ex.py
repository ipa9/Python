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