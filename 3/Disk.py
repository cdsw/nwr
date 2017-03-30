import turtle

class Disk:
    def __init__(self, name, xpos, ypos, h, w, c):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.h = h
        self.w = w  
        self.c = c
        self.t = t = turtle.Turtle()
    
    def showdisk(self):
        self.t.setheading(0)
        self.t.penup()
        self.t.goto(self.xpos, self.ypos)
        self.t.pendown()
        self.t.begin_fill()
        self.t.fillcolor(self.c)
        self.t.goto(self.xpos + self.w / 2, self.ypos)
        self.t.goto(self.xpos + self.w / 2, self.ypos + self.h)
        self.t.goto(self.xpos - self.w / 2, self.ypos + self.h)
        self.t.goto(self.xpos - self.w / 2, self.ypos)
        self.t.goto(self.xpos, self.ypos)
        self.t.penup()
        self.t.end_fill()

    def newpos(self, x, y):
        self.xpos = x
        self.ypos = y

    def cleardisk(self):
        self.t.setheading(0)
        self.t.penup()
        self.t.goto(self.xpos, self.ypos)
        self.t.clear()