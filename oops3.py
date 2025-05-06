# class b1:
#     def __init__(self):
#         super(b1,self).__init__()
#         print("Base class-1")
# class b2:
#     def __init__(self):
#         super(b2,self).__init__()       #Multiple inheritance
#         print("Base class-2")
# class derived(b1,b2):
#     def __init__(self):
#         super(derived,self).__init__()
#         print("Derived class from both class")
#
# d=derived()
#
# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add1(self):
#         return self.a+self.b
# class mul:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def mul1(self):
#         return self.a*self.b
# class calc(add,mul):
#     def __init__(self,a,b):
#         add.__init__(self,a,b)
#         mul.__init__(self,a,b)
#         print("Derived class initialized")           CALCULATOR EXAMPLE
#
# n1=int(input("Enter first value"))
# n2=int(input("Enter second value"))
# c=calc(n1,n2)
# print(add.add1(c))
# print(mul.mul1(c))


# class sq:
#     def __init__(self,a):
#         self.a=a
#     def squared(self):
#         return self.a**2
# class cub:
#     def __init__(self,a):
#         self.a=a
#     def cubed(self):
#         return self.a**3
#
# class main(sq,cub):
#     def __init__(self,a):
#         sq.__init__(self,a)
#         cub.__init__(self,a)
#
# n1=int(input("Enter a number"))
# o=main(n1)
# a=sq.squared(o)
# b=cub.cubed(o)
# print(a+b)


# class person:
#     def name(self):
#         print("Name")
# class teacher(person):
#     def qualification(self):
#         print("Phd")
# class hod(teacher):
#     def exp(self):
#         print("Experience")
# h=hod()
# h.name()
# h.qualification()
# h.exp()

# class num:
#     def __init__(self,n):
#         self.n=n
#         print("Number initialized")      Multi-level inheritance
# class sq(num):
#     def square(self):
#         return self.n**2
# class cu(sq):
#     def cubed(self):
#         return self.n**3
# cal=cu(10)
# print(sq.square(cal))
# print(cu.cubed(cal))

class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()

class mango(fruit):
    def taste(self):
        return "Sweet"
    def vitamin(self):
        return "Vitamin-A"
    def color(self):
        return "Yellow"
class orange(fruit):
    def taste(self):
        return "Sweet and Sour"
    def vitamin(self):
        return "Vitamin-C"
    def color(self):
        return "Orange"
A=mango()
print(A.color(),A.taste(),A.vitamin())
