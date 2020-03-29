class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        selectedItem = self.data[index]
        if not (self.length-1 == index):
            for i in range(index,self.length-1):
                self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1



arr=MyArray()
arr.push(20)
arr.push('safgsajkfb')
arr.push('badfv')
arr.push('hector')
arr.push('agfkokgonhhnmhn')
arr.pop()
arr.delete(3)
print(arr)