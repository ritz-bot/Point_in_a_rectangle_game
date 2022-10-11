#turtle is a python built in library used to generate built in graphics 
from random import randint
import turtle

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fall_in_rect(self,rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upperright.x \
        and rectangle.lowleft.y <self.y < rectangle.upperright.y:
            
            return True
        else:
            return False
class Rectangle:
    def __init__(self,lowleft,upperright):
        self.lowleft=lowleft
        self.upperright=upperright
    def area(self):
        return (self.upperright.x-self.lowleft.x) * (self.upperright.y-self.lowleft.y)
    

class GuiRectangle(Rectangle):#inheritance applied here(is-A and has-A)
    def draw(self,canvas):
        #now as myturtle is the instance of canvas we need to replace it everywhere
        canvas.penup()#the line is not printed
        canvas.goto(self.lowleft.x,self.lowleft.y)#self.lowleft.x,self.lowleft.y
        canvas.pendown()
        canvas.forward(self.upperright.x-self.lowleft.x)#moved 100 pixels
        canvas.left(90)#moved 90 pixels

        canvas.forward(self.upperright.y-self.lowleft.y)
        canvas.left(90)
        canvas.forward(self.upperright.x-self.lowleft.x )
        canvas.left(90)
        canvas.forward(self.upperright.y-self.lowleft.y)
        
        
class GuiPoint(Point):
    def draw(self,canvas,size=5,color='red'):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)
        
    
        
gui_rectangle=GuiRectangle(Point(randint(0,400),randint(0,400)),Point(randint(10,400),randint(10,400)))
myturtle=turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
print(gui_rectangle.area())



rectangle=GuiRectangle(Point(randint(0,400),randint(0,400)),Point(randint(10,400),randint(10,400)))

print("("+str(rectangle.lowleft.x) + "," + str(rectangle.lowleft.y)+")" + " and " + \
      "("+str(rectangle.upperright.x) +","+str(rectangle.upperright.y)+")" )

user_point=GuiPoint(float(input("Enter the number :x->")),float(input("Enter the number :y->")))
user_area=float(input("Guess the rectangle area :"))
print("our Point is in rectangle",user_point.fall_in_rect(rectangle))
print("rectangle area is ",abs(rectangle.area()))
print("Th area is off by ", abs(rectangle.area()-user_area))

myturtle=turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()

        
