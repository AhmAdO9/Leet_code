import random

class RandomizedSet(object):

    def __init__(self):
        self.values = {}
        self.li = []


    def insert(self, val):
        a = len(self.values) 
        self.values[val] = val
        if a == len(self.values):
            return False
        else:
            self.li.append(val)
            return True
    
  

    def remove(self, val):
        a = len(self.values) 
        try:
            p = self.values.pop(val)
        except KeyError:
                return False
        else:
            self.li.pop(self.li.index(p))
            return True

        

    def getRandom(self):
        r = random.choice(self.li)
        return r


obj = RandomizedSet()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.remove(1))
print(obj.remove(1))
print(obj.getRandom())
