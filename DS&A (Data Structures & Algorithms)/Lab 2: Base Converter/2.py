dict1 = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",
18:"I",19:"J",20:"K",21:"L",22:"M",23:"N",24:"O",25:"P",26:"Q",
27:"R",28:"S",29:"T",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}
def from_decimal(val,base):
    newlist = ""
    #quot = 0
    if (1 < base < 37 ) and val >= 0:
        while val >= 1:
            quot = val % base
            val = val // base
            if quot >= 10:
               quot_L = dict1[quot]
               newlist = newlist + quot_L
            else:
               newlist = newlist + str(quot)
        print(newlist[::-1])
    elif val < 0:
        print("ERROR! Negative num")
    elif not(1<base<37):
        print("ERROR! Invalid base.")
from_decimal(int(input("enter a number: ")),int(input("enter a base: ")))
def to_decimal(s, base):
    val = []
    result = 0
    status = False
    for i in s:
      if i.isnumeric():
        val.append(int(i))
      else:
        val.append(ord(i)-55)
    val = val[::-1]
    for i in range(0,len(val)):
      sum = val[i]*base**i
      result = result+sum 
    print(result)
to_decimal(str(input("Enter your value: ")),int(input("Enter your base: ")))

def to_decimal(s, base):
    val = []
    result = 0
    for i in s:
      if i.isnumeric():
        val.append(int(i))
      else:
        val.append(ord(i)-55)
    val = val[::-1]
    for i in range(0,len(val)):
      sum = val[i]*base**i
      result = result+sum
    print(result)
to_decimal('43103',36)
