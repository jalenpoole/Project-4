class Car:

    def __init__(self):
        self.items = []
    
    def Addtoqueue(self, item):
        self.items.insert(0,item)

    def Popfromqueue(self):
        return self.items.pop()
    
    def Sizeofqueue(self):
        return len(self.items)
    
c=Car()


print(c.Sizeofqueue())
c.Popfromqueue()
print(c.Sizeofqueue())
