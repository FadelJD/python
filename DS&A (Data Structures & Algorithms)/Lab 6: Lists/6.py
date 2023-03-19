import turtle
import random

pen = turtle.Turtle()

def start():
    pen.color("black")
    pen.speed(10)
    pen.penup()
    pen.setpos(-200,-200)
    pen.pendown()
    pen.forward(400)
    pen.backward(400)
    pen.left(90)
    pen.forward(400)
    pen.backward(400)
    pen.right(90)

start()

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
        self.coords = [self.x, self.y]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __repr__(self):
        return "".join(["(", str(self.x), ",", str(self.y), ")"])

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)

class line:
    def __init__(self, length,length2):
        self.length = length
        self.length2 = length2

    def listify(self):
        list1 = []
        list2 = []
        for i in range(self.length):
            list1.append(Point(random.randint(0,20), random.randint(0,20)).coords)
        for i in range(self.length2):
            list2.append(Point(random.randint(0,20), random.randint(0,20)).coords)
        return list1, list2, self.length2, "split"

    def join(self, list1, list2):
        list1.extend(list2)
        print("list1:", list1)
        print("list2:", list2)
        list2 = []
        return list1, list2, self.length2, "straight"

    def join2(self, list1, list2):
        for i in range(len(list2)):
            popped = list2.pop(0)
            list1.append(popped)
        print("list1:", list1)
        print("list2:", list2)
        return list1, list2, self.length2, "straight"
    def zigzag(self, list1, list2):
            if len(list1) > len(list2):
                longer = "list1"
                l = len(list1) - len(list2)
            elif len(list1) < len(list2):
                longer = "list2"
                l = len(list2) - len(list1)
            else:
                longer = "none"
                l = 0
            list3 = []
            a = 0
            while len(list1) > 0 or len(list2) > 0:
                if a == 0:
                    if len(list1) > 0:
                        list3.append(list1.pop(0))
                        a = 1
                    else:
                        a = 1
                if a == 1:
                    if len(list2) > 0:
                        list3.append(list2.pop(0))
                        a = 0
                    else:
                        a = 0
            print("list3:", list3)
            print("list1:", list1)
            print("list2:", list2)
            return list3, list2, [l,longer], "zig"
    def zigzag2(self, list1, list2):
        if len(list1) > len(list2):
            longer = "list1"
            l = len(list1) - len(list2)
        elif len(list1) < len(list2):
            longer = "list2"
            l = len(list2) - len(list1)
        else:
            longer = "none"
            l = 0
        index = 1
        while len(list2) > 0:
            list1.insert(index, list2.pop(0))
            index += 2
        print("list1:", list1)
        print("list2:", list2)
        return list1, list2, [l,longer], "zig"
def draw(list1, list2, l, m):
    pen.penup()
    pen.goto((list1[0][0] * 20) - 200, (list1[0][1] * 20) - 200)
    pen.dot(10)
    pen.pendown()
    pen.color("red")
    print("color: red")
    if len(list2) != 0:
        for i in list1:
            pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
            pen.dot(10)
            print("line1 point:", i)
        pen.penup()
        pen.color("green")
        print("color: green")
        pen.goto((list2[0][0] * 20) - 200, (list2[0][1] * 20) - 200)
        pen.pendown()
        for i in list2:
            pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
            pen.dot(10)
            print("line2 point:", i)
    else:
        if m == "zig":
            theline = "line1"
            pen.goto((list1[1][0] * 20) - 200, (list1[1][1] * 20) - 200)
            pen.dot(10)
            print("line1 point:", list1[0])
            list1.pop(0)
            list3 = []
            if l[1] == "list1":
                for i in range(l[0] - 1):
                    list3.append(list1.pop())
            elif l[1] == "list2":
                for i in range(l[0]):
                    list3.append(list1.pop())
            for i in list1:
                pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
                if theline == "line1":
                    color = "green"
                    pen.color("green")
                    theline = "line2"
                elif theline == "line2":
                    color = "red"
                    pen.color("red")
                    theline = "line1"
                pen.dot(10)
                print(theline + " point:", i, "color:", color)
            for i in reversed(list3):
                if l[1] == "list1":
                    pen.color("red")
                    pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
                    pen.dot(10)
                    print("line1 point:",i,"color: red")
                elif l[1] == "list2":
                    pen.color("green")
                    pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
                    pen.dot(10)
                    print("line2 point:", i, "color: green")
        else:
            theline = "line1"
            for i in list1:
                if len(list1) - list1.index(i) == l:
                    pen.color("green")
                    print("color: green ")
                    theline = "line2"
                pen.goto((i[0] * 20) - 200, (i[1] * 20) - 200)
                pen.dot(10)
                print(theline + " point: ", i)
n1 = int(input("length of line1: "))
n2 = int(input("length of line2: "))
j = line(n1,n2).listify()
print("list1:", j[0])
print("list2:", j[1])
draw(j[0],j[1],j[2],j[3])
print(j)
if input("continue: ") == "c":
    pen.clear()
    start()

class linetester:
    def __init__(self,l1, l2):
        self.l1 = l1
        self.l2 = l2

    def jointest(self):
        k = line(self.l1,self.l2).join(j[0],j[1])
        draw(k[0],k[1],k[2],k[3])

    def jointest2(self):
        k = line(self.l1,self.l2).join2(j[0],j[1])
        draw(k[0],k[1],k[2],k[3])

    def zigtest(self):
        k = line(self.l1,self.l2).zigzag(j[0],j[1])
        draw(k[0],k[1],k[2],k[3])

    def zigtest2(self):
        k = line(self.l1,self.l2).zigzag2(j[0],j[1])
        draw(k[0], k[1], k[2], k[3])

turtle.done()
