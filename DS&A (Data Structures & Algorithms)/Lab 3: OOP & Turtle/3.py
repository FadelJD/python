import turtle
Hr = -1
minute=  -1
seconds = -1
while not(0<=Hr<=23):
    Hr = int(input("hour: "))
    if not(0<=Hr<=23):
        print("ERROR hours!")
while not(0<=minute<=59):
    minute = int(input("minutes: "))
    if not(0<=minute<=59):
        print("ERROR minutes!")
while not(0<=seconds<=59):
    seconds = int(input("seconds: "))
    if not(0<=seconds<=59):
        print("ERROR seconds!")

pen2 = turtle.Turtle()
pen3 = turtle.Turtle()
pen4 = turtle.Turtle()
pen4.color("red")

def draw(p):
    p.goto(0, 0)
    p.right(dict1[p][0])
    p.pendown()
    p.forward(dict1[p][1])
    p.left(dict1[p][0])
    p.penup()
    p.ht()

totalsec = (Hr* 60 * 60) + (minute * 60) + seconds
hourangle = ((Hr/ 12 + (minute / 12) / 60 + ((seconds / 12) / 60) / 60) * 360) - 90
minuteangle = ((minute / 60 + (seconds / 60) / 60) * 360) - 90
secondangle = ((seconds / 60) * 360) - 90
dict1 = {pen2: [hourangle, 90], pen3: [minuteangle, 150], pen4: [secondangle, 180]}
clk = turtle.Turtle()
count = 0
clk.speed(9)
clk.up()
clk.color("navy blue")
clk.goto(0, -250)
clk.down()
clk.circle(250)
clk.up()
clk.color("dark green")
for i in range(12):
    clk.goto(0,0)
    if count == 0 or count % 3 == 0:
        clk.forward(200)
        clk.down()
        clk.forward(50)
    else:
        clk.forward(230)
        clk.down()
        clk.forward(20)
    clk.circle(0, 30)
    clk.up()
    count = count + 1
clk.goto(0,0)
clk.down()
clk.dot(10)
draw(pen2)
draw(pen3)
draw(pen4)
clk.ht()
turtle.done()

#Turtle Race task: Just remove the etra apostrophies for running this and instead add them on the previous code
'''
d = turtle.Turtle()
d.pu()
d.goto(-300,300)
d.pd()
d.forward(600)
d.write("FINISH")
t = turtle.Turtle()
t.penup()
t.color("red")
t.shape("turtle")
t.goto(-200,-250)
t.left(90)
t.pd()
s = turtle.Turtle()
s.penup()
s.color("green")
s.shape("turtle")
s.goto(0,-250)
s.left(90)
s.pd()
a = turtle.Turtle()
a.penup()
a.color("blue")
a.shape("turtle")
a.goto(200,-250)
a.left(90)
a.pd()
a_tank = 300
s_tank = 280
t_tank = 100
while True:
    if a_tank != 0:
        a.forward(11)
        a_tank = a_tank - 5
        a.write(a_tank)
    else:
        a.write("Energy gone")
    if s_tank != 0:
        s.forward(10)
        s_tank = s_tank - 5
        s.write(s_tank)
    else: 
        s.write("Energy gone")
    if t_tank != 0:
        t.forward(15)
        t_tank = t_tank - 5
        t.write(t_tank)
    else:
        t.write("Energy gone")
    if a.ycor() == 300:
        a.write("winner is BLUELU")
        break
turtle.done()
'''
