# class abc:
#     var=5
#     def a(self):
#         print("Hello")
# obj=abc()
# print(obj.var)
# obj.a()

#CONSTRUCTOR
# class a:
#
#     def __init__(self,val):
#         self.val=val
#         print(val)
#
# obj=a(10)

# class check:
#
#     def check_even_odd(self,val):
#         if val%2 == 0:
#             self.flag=0
#         else:
#             self.flag=1
#     def e_o(self,val):
#         self.check_even_odd(val)
#         if self.flag==0:
#             print("Even")
#         else:
#             print("odd")
#
#
# obj=check()
# obj.e_o(10)
#
# class number():
#     def __init__(self,val):
#         self.val=val
#         self.l=[]
#         self.l1=[]
#     def even_list(self):
#         if self.val%2 == 0:
#             self.l.append(self.val)
#         else:
#             self.l1.append(self.val)
#     def display(self):
#         print(self.l)
#         print(self.l1)
# n1=number(21)
# n1.even_list()
# n1.display()
# n1=number(32)
# n1.even_list()
# n1.display()
# n1=number(43)
# n1.even_list()
# n1.display()
# n1=number(54)
# n1.even_list()
# n1.display()
# n1=number(65)
# n1.even_list()
# n1.display()

# class abc():
#     def __init__(self,name,var):
#         self.name=name
#         self.var=var
#     def __repr__(self):
#         return repr(self.var)
#     def __len__(self):
#         return len(self.name)
#     def __cmp__(self, obj):
#         return self.var - obj.var
# obj=abc("abcdef",10)
# print("The value stored in object is", repr(obj))
# print("length",len(obj))
# obj1=abc("ghijklkk",11 )
# val=obj.__cmp__(obj1)
# if val==0:
#     print("equal")
# elif val==-1:
#     print("first value is less than second")
# else:
#     print("second value is less than first")