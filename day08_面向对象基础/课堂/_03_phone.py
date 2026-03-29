class Phone:
    def open(self):
        print(f"{self.name}open")
    def close(self):
        print(f"{self}close")
    def take_photo(self):
        print(f"{self}take_photo")
    def fun(self):
        self.open()
        self.take_photo()
        self.close()

p1 = Phone()
p1.name = "iphone"
print(p1.name)
p1.fun()
print("------")
p2 = Phone()
print(p2.name)