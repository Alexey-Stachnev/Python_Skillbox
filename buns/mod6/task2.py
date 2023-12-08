class DoubleElement:
    def __init__(self, *lst):
        self.list = lst
        self.counter = 0

    def __next__(self):
        if self.counter == len(self.list) - 1:
            result = (self.list[self.counter], None)
            self.counter += 2
            return result
        elif self.counter < len(self.list):
            result = (self.list[self.counter], self.list[self.counter + 1])
            self.counter += 2
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)
