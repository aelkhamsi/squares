from HashTable import HashTable
import time
import random

HASHTABLE_SIZE = 10000

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x=' + str(self.x) + ', y=' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # tupleRepr = (self.x, self.y)
        # return tuple.__hash__(tupleRepr)

        # return hash(self.x) ^ hash(self.y)

        return hash(self.x * 10**32) ^ hash(self.y * 10**31)



# Store all the points in a hash table
hashTable = HashTable(HASHTABLE_SIZE)
points = []

with open('points.txt', 'r') as f:
    line = f.readline()
    while line:
        [x, y] = line.split()
        point = Point(int(x), int(y))
        hashTable.insert(point)
        points.append(point)
        line = f.readline()

# print(hashTable.maxCollisions())
# print(hashTable)


num_squares = 0
cnt=0
start = time.time()

for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        a = points[i]
        b = points[j]
        trsf_x = b.x - a.x
        trsf_y = b.y - a.y

        #1st square (a, b, p1, p2)
        p1 = Point(a.x + trsf_y, a.y - trsf_x)
        p2 = Point(b.x + trsf_y, b.y - trsf_x)
        if (hashTable.search(p1) and hashTable.search(p2)):
            cnt+=1
            if (cnt == 4):
                cnt=0
                num_squares += 1
                consolePrint = "Number of squares: " + str(num_squares) + "..."
                print (consolePrint, end="\r")

        #2nd square (a, b, p3, p4)
        p3 = Point(a.x - trsf_y, a.y + trsf_x)
        p4 = Point(b.x - trsf_y, b.y + trsf_x)
        if (hashTable.search(p3) and hashTable.search(p4)):
            cnt+=1
            if (cnt == 4):
                cnt=0
                num_squares += 1
                consolePrint = "Number of squares: " + str(num_squares) + "..."
                print (consolePrint, end="\r")


end = time.time() - start
print("Number of squares: " + str(num_squares))
print("Total time (in seconds): ", end)
