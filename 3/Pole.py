import turtle as t


class Pole:
    def __init__(self, name, x, y):
        self.name = name
        self.length = 100
        self.thickness = 30
        self.topPosition = 0
        self.x = x
        self.y = y
        self.stack = []
        self.color = 'lightblue'

    def showpole(self):
        self.tt = t.Turtle()
        self.tt.hideturtle()
        self.tt.speed(10)
        self.tt.color(self.color)
        self.tt.setheading(0)
        self.tt.pu()
        self.tt.goto(self.x, self.y)
        self.tt.pd()
        self.tt.begin_fill()
        
        # DRAW POLE
        self.tt.fd(self.thickness/2)
        self.tt.lt(90)
        self.tt.fd(self.length)
        self.tt.lt(90)
        self.tt.fd(self.thickness)
        self.tt.lt(90)
        self.tt.fd(self.length)
        self.tt.lt(90)
        self.tt.fd(self.thickness/2)

        self.tt.end_fill()

    def pushdisk(self, disk):
        self.stack.append(disk)
        self.topPosition += 1
        
        disk.cleardisk()
        disk.newpos(self.x, disk.h*(self.topPosition-1) )
        disk.showdisk()


    def popdisk(self):
        disk = self.stack.pop()
        self.topPosition -= 1
        disk.cleardisk()
        disk.newpos(self.x, self.y+20)
        disk.showdisk()
        return disk