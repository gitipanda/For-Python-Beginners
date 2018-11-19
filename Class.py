# This is practice for learning "Class"
# ------------------Example 1-----------------------
# 初见 class
class Employee:
    pass  #Think: why we have "pass"? otherwise cannot run?

john = Employee()  # Create an empty employee record named "John"

# Fill the properties of the record "John"
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
john.mum='ppy'
print('John\'s name is '+john.mum)
print("Example1 ends, this is first touch of class~")

# ------------------Example 2----------------------
# Setvalue, Getvalue, link to dict

class Sample:
    def setValue(self, val,num):
        self.val = val
        self.num = num
    def getValue(self):
        return self.val+str(self.num) # change var-type

# (1)setvalue, getvalue
s = Sample()                      # create a record in class
s.setValue("Hello World!",2)
print(s.getValue())
#out: Hello World!
#re-setvalue
s=Sample()
s.val="Welcome"
s.num=3
print(s.getValue())
#out: Welcome

#(2) link to dict
print(s.__dict__)     #s' dict
#{'val':'Welcome'}
print(s.__dict__.get("val")) #get value w.r.t "val"
#Welcome
print(s.__dict__.get("num")) #get value w.r.t "vall"
#hi

#re-setvalue
Sample.setValue(s, "value init",5)  # 类似于s.setValue("value init")
print(s.getValue())
#value init
print("Example3 ends, setvalue, getvalue, link to dict")



# ----------------Example 3----------------------------
# init/default setting
class Shape:
   def __init__(self, x, y, w=10, h=10):
       self.x = x
       self.y = y
       self.width = w
       self.height = h

s = Shape(4, 5)                 # width和height采用默认值
print("dict(1) is:"+str(s.__dict__))

s = Shape(4, 5, 100)
print("dict(2) is:"+str(s.__dict__))

s = Shape(4, 5, w=50, h=45)     # 采用混合参数
print("dict(3) is:"+str(s.__dict__))

print("Example3 ends, set default for a class")



#-----------------Example 4--------------
# Father-class
print(Shape.__dict__)
print("Shape bases is"+str(Shape.__bases__))
class Circle(Shape):            # Cirle继承Shape类
    pass
print("Circle"+str(Circle.__bases__))
class Oval(Shape,Sample,Employee):
    pass
print("Oval"+str(Oval.__bases__))
# Father property defines son's properties
Shape.color="red"
s1=Shape(3,4)
s2=Shape(5,6)
print(Shape.color,s1.color,s2.color)
Shape.color="blue"
print(Shape.color,s1.color,s2.color)
#however, son can change itself
s1.color=1
print(Shape.color,s1.color,s2.color)
print("Example4 ends, define inherent class; father-calss defines son; son can change itself")


# ----------------Example 5-----------------
# Set method, method reload
def draw(self):
    print("position at (%d, %d)" % (self.x, self.y))
Shape.draw = draw
Shape.draw(s1)
s2.draw()

class Samfun:
    def add(self,val1,val2):
        return val1+val2
    def add(self,val1,val2,val3):
        return val1+val2+val3
s= Samfun()
# print("13+23="+str(s.add(13,23)))
# wrong: since method is already reloaded
print("13+23+33="+str(s.add(13,23,33)))
print("Example5 ends")

#-------------------Example 6-----------------------------
# Example 6 : How to use the defined function Reverse?
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]



A =  Reverse(["banana","apple","hi"])
B=[]
for i in range(3):
    B.append(A.__next__())
print(B)

print("Example6 ends")


# print(A.data)
# print(A.index)
# B=([A.__next__()])
# print(B)
# B.append(A.__next__())
# print(B)
# B.append(A.__next__())
# print(B)






