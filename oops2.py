# class abc():
#     def __init__(self,var):
#         self.__var=var
#     def __display(self):                 Private variable,class
#         print(self.__var)
# a=abc(10)
# a._abc__display()


# class abc:
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("Value is:",self.var)       Local method value through local method
#     def adds(self):
#         self.var+=20
#         self.display()
#
# a=abc(10)
# a.adds()

# def out(x):
#     return x*10
#
#
# class abc:
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("Value is:",self.var)         calling outside function by class method
#     def modify(self):
#         self.var=out(self.var)
#
# a=abc(20)
# a.display()
# a.modify()
# a.display()

# class abc:
#     def __init__(self,var):
#         self.var=var
#     def display(self):
#         print("value is:",self.var)
# a=abc(10)
# a.display()
# print(hasattr(a,'var'))
# getattr(a,'var')
# setattr(a,'var',55)
# print("After setting",a.var)             Built-in Functions
# setattr(a,'new_var',100)
# print("new var:",a.new_var)
# delattr(a,'var')

#
# ._doc__ > when string doc is not specified return attributes
# .__dict__namespace accessed attributes
# .__name__ return class attributes name
# .__module__
# .__bases__

# class abc:
#     def __init__(self,var,var1   ):
#         self.var=var
#         self.var1=var1
#         self.v3=v3
#     def display(self):
#         print("value is:",self.var,self.var1)
# a=abc(10,20)
# a.display()
# print("obj dict",a.__dict__)
# print("doc",a.__doc__)
# print("class name",abc.__name__)
# print("obj module",a.__module__)
# print("bases",abc.__bases__)


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def add_marks(self):
#         for i in range(3):
#             a=int(input("Enter %s marks in %d subject:"%(self.name,i+1)))
#             self.marks.append(a)
#     def display(self):
#         print(f"{self.name} got {self.marks}")
#
# a=student("vijay",[])
# a1=student("Anil",[])
# a.add_marks()
# a1.add_marks()
# a.display()
# a1.display()

# class Circle:
#     pi=3.14159
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         print("Area of circle:",Circle.pi*self.radius*self.radius)
#     def circum(self):
#         print("Circumference of circle:",2*Circle.pi*self.radius)
# c1=Circle(7.5)
# c1.area()
# c1.circum()


