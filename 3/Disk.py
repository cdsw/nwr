import turtle

class Disk:
    def __init__(self, name, xpos, ypos, h, w, c):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.h = h
        self.w = w  
        self.c = c
    
    def showdisk(self):
        t = turtle.Turtle()
        t.setheading(0)
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.begin_fill()
        t.fillcolor(self.c)
        t.goto(self.xpos + self.w / 2, self.ypos)
        t.goto(self.xpos + self.w / 2, self.ypos + self.h)
        t.goto(self.xpos - self.w / 2, self.ypos + self.h)
        t.goto(self.xpos - self.w / 2, self.ypos)
        t.goto(self.xpos, self.ypos)
        t.penup()
        t.end_fill()

    def newpos(self, x, y):
        self.xpos = x
        self.ypos = y

    def cleardisk(self):
        t = turtle.Turtle()
        t.setheading(0)
        t.penup()
        t.goto(self.xpos, self.ypos)
        t.pendown()
        t.pencolor("white")
        t.begin_fill()
        t.fillcolor("white")
        t.goto(self.xpos + self.w / 2, self.ypos)
        t.goto(self.xpos + self.w / 2, self.ypos + self.h)
        t.goto(self.xpos - self.w / 2, self.ypos + self.h)
        t.goto(self.xpos - self.w / 2, self.ypos)
        t.goto(self.xpos, self.ypos)
        t.penup()
        t.end_fill()