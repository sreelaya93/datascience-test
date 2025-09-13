# class Sample:
#     def __init__(self,name):
#         self.name=name
# class S1(Sample):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age=age
#     def show(self):
#         print('enter your name : ',self.name)
#         print('enter your age : ',self.age)
# obj=S1('aaa',30)
# obj.show()

#-----------------------------------------------------------------------------------------------------

# total=lambda x:x+x
# print(total(50))

#-----------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class Stud(Student):
#     def __init__(self,name,roll,m1,m2,sum):
#         super().__init__(name,roll)
#         self.m1=m1
#         self.m2=m2
#         self.sum=sum
#     def cal(self):
#         self.sum=self.m1+self.m2
#     def show(self):
#         print('my name is ',self.name, 'my roll no is ',self.roll, 'total mark is ',self.sum)
# s=Stud('dev',16,56,78,0)
# s.cal()
# s.show()

#-------------------------------------------------------------------------------------------------------

# class Vehicle:
#     def __init__(self,type,color,number):
#         self.type=type
#         self.color=color
#         self.number=number
#     def output(self):
#         print('my vehicle is ',self.type,'its color is',self.color,'its number is ',self.number)
# class MyVehicle(Vehicle):
#     def show(self):
#         print('my vehicle is a car')
# v=MyVehicle('car','white','456')
# v.output()

#---------------------------------------------------------------------------------------------------------

# class Student():
#     def __init__(self,name,m1,m2,sum):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.sum=sum
# class Stud(Student):
#     def calc(self):
#         self.sum = self.m1 + self.m2
#         return self.sum
#     def show(self):
#         print('name : ',self.name)
#         print('mark : ',self.sum)
# s=Stud('dev',45,89,0)
# s.calc()
# s.show()

#---------------------------------------------------------

class Student:
    def __init__(self,name,roll,m1,m2,sum):
        self.name=name
        self.roll=roll
        self.m1=m1
        self.m2=m2
        self.sum=sum
class Stud(Student):
    def cal(self):
        self.sum=self.m1+self.m2
    def show(self):
        print('my name is ',self.name, 'my roll no is ',self.roll, 'total mark is ',self.sum)
s=Stud('dev',16,56,78,0)
s.cal()
s.show()