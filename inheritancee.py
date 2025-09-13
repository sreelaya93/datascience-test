#class Car:
#     a1="BMW"
#     a2="series1"
#     def fun(self):
#        print('im from',self.a1)
#        print('my model is',self.a2)##

#john=Car()
#print(john.a1)
#print(john.a2)
#john.fun()

#----------------------------------------------------------------------------------

#class Person:
#    def __init__(self,name):
#        self.name=name
#    def show(self):
#       print('hello,my name is ',self.name)

#p=Person('vignesh')
#p.show()
#---------------------------------------------------------------------------------

#class Person:
#    def __init__(self,name,age):
#        self.name=name
#        self.age=age
#    def dtls(self):
#        print('my name is ',self.name)
#        print('age is ',self.age)

#p1=Person('john',10)
#p2=Person('vignesh',12)
#p1.dtls()
#p2.dtls()
#p1.age=90
#p1.dtls()
#-------------------------------------------------------------------------------

#class Myclass:
#    def __init__(self):
#        self.hello='hello'
#    def show(self):
#        print(self.hello)
#obj=Myclass()
#obj.show()
#--------------------------------------------------------------------------------

# class A:
#
#     def __init__(self,n1,n2,sum):
#         self.n1=n1
#         self.n2=n2
#         self.sum=sum
#     def show(self):
#         self.sum=self.n1+self.n2
#         print('sum of numbers ',self.sum)
# obj=A(1000,2000,sum=0)
# obj.show()
#---------------------------------------------------------------------------------

# class Employee:
#     def __init__(self):
#         print('employee created')
#     def __del__(self):
#         print('destructor called')
# def create_obj():
#     print('making object')
#     obj=Employee()
#     print('function end')
#     return obj
# print("calling create_obj function")
# obj=create_obj()
# print('program end')

#-------------------------------------------------------------------------------

# class Person(object):
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def isEmployee(self):
#         return False
# class Employee(Person):
#     def isEmployee(self):
#         return True
#
# emp=Person('sathya')
# print(emp.getName(),emp.isEmployee())
# emp=Employee('vig')
# print(emp.getName(),emp.isEmployee())

#---------------------------------------------------------------------------------

# class Base():
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# class Child(Base):
#     def __init__(self,name,age):
#         Base.__init__(self,name)
#         self.age=age
#     def getAge(self):
#         return self.age
# class GndChild(Child):
#     def __init__(self,name,age,adrs):
#         Child.__init__(self,name,age)
#         self.adrs=adrs
#     def getAdrs(self):
#         return self.adrs
# g=GndChild('aaa',20,'kannur')
# print(g.getName(),g.getAge(),g.getAdrs())

#----------------------------------------------------------------------------------

# class Animal:
#     def speak(self):
#         pass
# class Dog(Animal):
#     def speak(self):
#         return 'wolf'
# class Cat(Animal):
#     def speak(self):
#         return 'meow'
# dog=Dog()
# cat=Cat()
# print(dog.speak())
# print(cat.speak())

#-------------------------------------------------------------------------------------------

# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         import math
#         return math.pi * self.radius ** 2
# rect=Rectangle(5,4)
# c=Circle(3)
# print(rect.area())
# print(c.area())

#----------------------------------------------------------------------------------------------------

# class Emp:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def show(self):
#         return f"{self.name}: ${self.salary}"
# class Mng(Emp):
#     def __init__(self,name,salary,dept):
#         super().__init__(name,salary)
#         self.dept=dept
#     def show(self):
#         return f"{self.name}(Mng): ${self.salary},Dept:{self.dept}"
# emp1=Emp('aaa','10000')
# mng1=Mng('bbb',20000,'sales')
# print(emp1.show())
# print(mng1.show())