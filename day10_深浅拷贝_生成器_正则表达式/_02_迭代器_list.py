class myListInter():
    def __init__(self,list = [],step=1):
        self.list = list
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration

        current = self.start
        self.start += self.step
        return current


if __name__ == '__main__':

    myRange = myListInter([1, 2, 3, 4, 5])
    for item in myRange:
        print(item)
