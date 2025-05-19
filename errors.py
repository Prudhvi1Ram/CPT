# 5/0 #ZeroDivisioError
# "A"+5 "TypeError"
# print(x) #NameError


# n=int(input("Enter numerator"))
# d=int(input("Enter denominator"))
# try:
#     q=n/d
#     print("Quotient is:",q)
# except ZeroDivisionError:
#     print("Denominator cant be zero")

# try:
#      a=int(input("Enter a number"))
#      print(a**2)
# except KeyboardInterrupt:
#     print("Enter a number not space")
# except ValueError:
#     print("check before you enter")
# print("Bye")


# try:
#      a=int(input("Enter a number"))
#      print(a**2)
# except (KeyboardInterrupt,TypeError,ValueError):
#     print("Enter a number ")

# try:
#     n=5
#     print(n)
#     raise ValueError
# except:
#     print("Raised an error even after normal execution")

#
# try:
#     raise Exception('hi','a')
# except Exception as erroroj:           class exception
#     print(type(erroroj))
#     print(erroroj)
#     print(erroroj.args)
#     x,y=erroroj.args
#     print(x,y)

# def div(n,d):
#     try:
#         print(n/d)
#     except ZeroDivisionError:
#         print("Denominator cant be zero")
#
# a=int(input("Enter num"))
# b=int(input("Enter den"))
# div(a,b)

'''
inbuilt-exceptions
Exception-base class
systemExit-sys.exit()
StandardError-except sys.exit()/StopIteration
OverflowError-numeric type errors exceeds limit
ArithmeticError-Base class for all calculations
IoError-import file error
LookupError
EOFError
StopIterationError
SyntaxError
SystemError
IndentationError
'''
from webbrowser import Error


# class myError(Exception):
#     def __init__(self,value):
#         self.value=value
#     def __str__(self):
#         return repr(self.value)
# try:
#     raise myError(8)
# except Exception as e:
#     print(e)

# try:
#     print("ABC")
#     raise ValueError
# except ValueError:
#     print(1)
# finally:
#     print("Ab")
#

# class calculator:
#     # def __init__(self,a,b):
#     #     self.a=a
#     #     self.b=b
#     def input_numbers(self):
#         try:
#             self.a=float(input("Enter 1st number"))
#             self.b = float(input("Enter 2nd number"))
#         except ValueError:
#             print("Enter some number")
#             self.input_numbers()
#     def add(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def sub(self):
#         return self.a-self.b
#     def div(self):
#         return self.a/self.b
#     def expo(self):
#         return self.a**self.b
#     def floor_div(self):
#         return self.a//self.b
#     def modulo(self):
#         return self.a%self.b
#
# def display_menu():
#     print("\n --> Calculator menu <--")
#     print("1. Addition")
#     print("2. Multiplication")
#     print("3. Subtraction")
#     print("4. Division")
#     print("5. Exponent")
#     print("6. Modulus")
#     print("7. floor-division")
#     print("8. Exit")
#
#
#
# def main():
#     calc=calculator()
#     while True:
#         display_menu()
#         choice=input("Enter a choice(1-8)")
#         if choice == "8":
#             print("Exit")
#             break
#         calc.input_numbers()
#         try:
#             if choice == "1":
#                 print("Result",calc.add())
#             elif choice == "2":
#                 print("Result",calc.sub())
#             elif choice == "3":
#                 print("Result",calc.mul())
#             elif choice == "4":
#                 print("Result",calc.modulo())
#             elif choice == "5":
#                 print("Result",calc.div())
#             elif choice == "6":
#                print("Result",calc.expo())
#             elif choice == "7":
#                print("Result",calc.floor_div())
#             else:
#                   print("Invalid input")
#         except ZeroDivisionError:
#                 print("Denominator cant be zero")
#         except Error:
#                 print("Unexpected error")
#
# main()
