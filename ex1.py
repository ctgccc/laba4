class List:
    def __init__(self):
        self.items=[]

    def add(self, val):
        self.items.append(val)

    def remove(self, val):
        if val in self.items:
            self.items.remove(val)

    def search(self, val):
        if val in self.items:
            return True
        return False

    def get_size(self):
        return len(self.items)

    def clear(self):
        self.items=[]

a_list=List()

a_list.add(3)
a_list.add(7)
a_list.add(18)
print(a_list.get_size())
a_list.remove(7)
print(a_list.search(20))
a_list.clear()
print(a_list.get_size())