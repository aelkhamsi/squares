import random

class HashTable:
        def __init__(self, size):
                self.size = size
                self.map = [None] * self.size

        def hashCode(self, obj):
            return obj.__hash__() % self.size
            # return hash(obj) % self.size


        def insert(self, obj):
                index = self.hashCode(obj)

                if self.map[index] is None:
                    self.map[index] = [obj]
                    return True
                else:
                    self.map[index].append(obj)
                    return True

        def search(self, obj):
                index = self.hashCode(obj)

                if self.map[index] is not None:
                    for elem in self.map[index]:
                            if elem == obj:
                                return True
                return False

        def delete(self, obj):
                index = self.hashCode(obj)

                if self.map[index] is not None:
                    for i in range (len(self.map[index])):
                            if self.map[index][i] == obj:
                                    self.map[index].pop(i)
                                    return True
                return False

        def maxCollisions(self): #dev
            max=0
            for i in range(len(self.map)):
                if (self.map[i] is not None):
                    length = len(self.map[i])
                    if (length > max):
                        max = length
            return max

        def getElement(self):
            return self.map[0][0]

        def __str__(self):
            for i in range(len(self.map)):
                print(i, ": ", self.map[i])
