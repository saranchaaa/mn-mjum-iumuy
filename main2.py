class Counter:
    def __init__(self, m):
        self.i = 0
        self.m = m

    def __iter__(self):
        self.i = 2
        return self

    def __next__(self):
        self.i *= 2

        if self.i > self.m:
            raise StopIteration
        return self.i

infinite = 9999999999999999999999999999999999999999999999999999
counter = Counter(infinite)

for i in counter:
    print(i)
