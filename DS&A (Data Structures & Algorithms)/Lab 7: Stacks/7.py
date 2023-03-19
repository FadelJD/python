import random

class Stack():
    #el_list = [] 
    def __init__(self, el_list, top, el_size):
        self.el_list = el_list
        self.top = top
        self.el_size = el_size

    def push(self, item):
        self.item = item
        if self.top + 1 > self.el_size:
            return "Cannot Push, its full"
        else:
            return self.el_list.append(self.item)

    def is_empty(self):
        if self.top < 0:
            return True
        else:
            return False

    def pop(self, popd_item):
        self.popd_item = popd_item
        if Stack.is_empty() == True:
            return "Cannot pop empty stack"
        else:
            self.popd_item = self.top
            self.el_list.pop(self.top)
            return self.popd_item

    def peek(self):
        return self.el_list[::-1]

    def size(self):
        return len(self.el_list)

    def contain(self, object):
        self.object = object
        for i in self.el_list:
            if i == self.object:
                print("contains element at position:%s", self.el_list(i))
                return True
            else:
                return False


class valet:
    def __init__(self, cars):
        self.cars = cars

    def park(self):
        carlist = random.sample(range(-1,999),self.cars)
        for i in range(len(carlist)):
            if carlist[i] < 100 and carlist[i] >= 10:
                carlist[i] = "0" + str(carlist[i])
            elif carlist[i] < 10:
                carlist[i] = "00" + str(carlist[i])
            else:
                carlist[i] = str(carlist[i])
        print(carlist)
        return carlist

def get(stack1, carwanted):
    stack2 = []
    if carwanted in stack1:
        for i in reversed(stack1):
            if carwanted != i:
                print("stack1:", stack1, "  stack2:", stack2)
                stack2.append(stack1.pop())
            else:
                print("stack1:", stack1, "  stack2:", stack2)
                order = str(stack1.index(i))
                result = stack1.pop()
                break
        print("found")
        for i in range(len(stack2)):
            print("stack1:", stack1, "  stack2:", stack2)
            stack1.append(stack2.pop())
        print("stack1:", stack1, "  stack2:", stack2)
    else:
        print("car not found")
        result = "none"
        order = "N/A"
    print(f'')
    print("stack1:", stack1)
    print("stack2:", stack2)
    print("result:", result, ", at index", order)

while True:
    try:
        n = int(input("cars: "))
        if n >= 0 and n < 1001:
            break
        else:
            print("invalid number")
    except ValueError:
        print("invalid input")

p = valet(n).park()

while True:
    try:
        w = int(input("want: "))
        if w >= 0 and w < 1000:
            if w < 100 and w >= 10:
                w = "0" + str(w)
            elif w < 10:
                w = "00" + str(w)
            else:
                w = str(w)
            break
        else:
            print("invalid number")
    except ValueError:
        print("invalid input")

get(p, w)


#FEEDBACK: ***

# 1) Try implementing get function in Class Valet
# 64011748

