
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata
        
    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def listify(self):
        thelist = []
        current = self.head
        while current != None:
            currentdata = current.getData()
            thelist.append(currentdata)
            current = current.getNext()
        return thelist

    def squish(self):
        current = self.head
        currenthead = current
        number = current.getData()
        current = current.getNext()
        while current != None:
            currentdata = current.getData()
            if currentdata != number:
                currenthead.setNext(current)
                currenthead = current
                number = currenthead.getData()
            current = current.getNext()

    def dble(self):
        current = self.head
        while current != None:
            currentdata = current.getData()
            newnode = Node(currentdata)
            newnode.setNext(current.getNext())
            current.setNext(newnode)
            current = current.getNext().getNext()

customlist1 = list(input("squishers: "))
customlist2 = list(input("dblers: "))
list1 = UnorderedList()
list2 = UnorderedList()
for i in reversed(customlist1):
    list1.add(i)
for i in reversed(customlist2):
    list2.add(i)

print("list1 size:", list1.size())
print("list1: ", list1.listify())
list1.squish()
print("list1 squish size: ", list1.size())
print("list1 squish:", list1.listify(),"\n")
print("list2 size:", list2.size())
print("list2: ", list2.listify())
list2.dble()
print("list2 dble size: ", list2.size())
print("list2 dble:", list2.listify())









#Post Lab
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  #initialize next node
        self.p = None  #initialize previous node

class golf_players:
    def __init__(self):
        self.head = None  #head

    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head 
        if self.head is not None:
            self.head.p = NewNode
        self.head = NewNode

    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.p = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.p = last
        return

    def insert(self, p_node, NewVal):
        if p_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = p_node.next
        p_node.next = NewNode
        NewNode.p = p_node
        if NewNode.next is not None:
            NewNode.next.p = NewNode

    def sortscore(self, name, score):
        current = self.head
        if current == None or score < self.head.data[1]:
            self.push([name, score])
            return
        else:
            currentdata = current.data[1]
            while current != None:
                if score >= currentdata:
                    current = current.next
                    if current == None:
                        self.append([name,score])
                        return
                    else:
                        currentdata = current.data[1]
                else:
                    self.insert(current.p,[name,score])
                    return

    def delete(self, name):
        current = self.head
        if current.data[0] == name:
            self.head = current.next
            return
        current = self.head
        while current != None:
            if current.data[0] == name:
                current.p.next = current.next
                return
            else:
                current = current.next
        print("Error!")

    def update(self, name, score):
        current = self.head
        while current != None:
            currentname = current.data[0]
            if currentname == name:
                current.data[1] = score
                if current.p == None:
                    self.head = current.next
                    self.sortscore(name,current.data[1])
                else:
                    current.p.next = current.next
                    self.sortscore(name, current.data[1])
                return
            current = current.next
        print("Error!")

    def retrieve(self,name):
        current = self.head
        while current != None:
            currentname = current.data[0]
            if name == currentname:
                print("players with same scores as", name)
                currentscore = current.data[1]
                print(current.data)
                next = current.next
                prev = current.p
                while prev != None and prev.data[1] == currentscore:
                    print(prev.data)
                    prev = prev.p
                while next != None and next.data[1] == currentscore:
                    print(next.data)
                    next = next.next
                return
            current = current.next
        print("Error!")

    def listify(self):
        thelist = []
        current = self.head
        while current != None:
            currentdata = current.data
            thelist.append(currentdata)
            current = current.next
        print(thelist)

    def revlistify(self):
        thelist = []
        current = self.head
        while current != None:
            currentdata = current.data
            thelist.append(currentdata)
            current = current.next
        thelist.reverse()
        print(thelist)

func = golf_players()
func.sortscore("Krasinski", 20)
func.sortscore("Joseph", 77)   
func.sortscore("Mukesh", 47)
func.sortscore("Philips", 59)
func.sortscore("Daniel", 41)
func.sortscore("Liz", 47)
func.sortscore("Ariana", 77)
func.sortscore("Katy", 61)
func.listify()
func.revlistify()
func.retrieve("Mukesh")
func.retrieve("Joseph")
func.delete("Daniel")
func.delete("Joseph")
func.listify()
func.update("Philips", 96)
func.update("Krasinski", 64)
func.listify()
