# def h(a="Ryan"):
#     print("Hello",a)
#
# h("Gosling")                 Overloading
# h()

#
# def abc(*args):
#     return sum(args)              Multiple args overloading
#
# print(abc(1,2,3,4,5,6))


# class student:
#     def __init__(self,name=None,age=None):
#         if name and age:
#             print(name,age)
#         elif age:
#             print(age)
#         else:
#             print("No data")
# student()
# student("Ryan",20)
# student("",30)

# class val:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,ol):
#         return val(self.x+ol.x,self.y+ol.y)
#     def __str__(self):
#         return f"{self.x},{self.y}"
# a=val(1,2)
# b=val(3,5)
# c=val(10,11)
# print(a+b+c)


# class complex:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, ol):
#         if isinstance(ol,complex):
#             return complex(self.x+ol.x,self.y+ol.y)
#         else:
#             raise TypeError("Unsupported operand type")
#     def __str__(self):
#         return f"{self.x}+{self.y}i"
# a=complex(1,2)
# b=complex(3,4)
# print(a+b)


# class pet:
#     def sound(self):
#         print("Speaks")
# class dog(pet):
#     def sound(self):
#         print("Barks")
# d=dog()
# d.sound()


# class pet:
#     def sound(self):
#         print("Speaks")
# class dog(pet):
#     def sound(self):
#         super().sound()
#         print("Barks")
# d=dog()
# d.sound()

# class student:
#     def __init__(self,name):
#         self.name=name
#         print("Student constructor")
# class person(student):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
#         print(self.grade)
# s=person("Ryan","A")


# class pet:
#     def sound(self):
#         print("Animal Sound")
# class dog:
#     def sound(self):
#         print("Barks")
# class cat:
#     def sound(self):
#         print("Meows")
# pets=[dog(),cat(),pet()]
# for i in pets:
#     i.sound()


class shape:
    def area(self):
        print("Nothing defined")

class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius**2*3.145

rad=int(input("Enter radius"))
shap=int(input("Enter shape"))
sq=square(shap)
ci=circle(rad)
print(sq.area())
print(ci.area())