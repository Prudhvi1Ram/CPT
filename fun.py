# def a(x,y=2):
#      return x*y
# print(a(5))
# print(a(5,3))


#
# def summ(*args):
#     return min(args),max(args),sum(args) / len(args)        #exercise
#
# a,b,c=summ(1,2,3,4,5)
# print(f"Min_value:{a},Max_value:{b},Avg_value:{c}")
# print(summ(10,202,30,22,3,4,1,2))


# def show(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
#
# show(name="Ryan",age=20,city="Denmark")


# add=lambda x,y=4:x+3+y
# print(add(3))



 #Recursions - direct, indirect, head, tail, linear, binary, divide and conquer, absolute, multiple, nested, tree

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))
# print(fact(0))

# def is_even(n):
#     if n==0:
#         return True
#     return is_odd(n-1)
#
# def is_odd(n):
#     if n==0:
#         return False
#     return is_even(n-1)
#
# print(is_even(6))
# print(is_odd(8))
#
# def is_palindrome(a):
#     if len(a) <=1:
#          return True
#     return check_palindrome(a,0,len(a)-1)
# def check_palindrome(a,start,end):
#      if start>=end:
#          return True
#      if a[start] != a[end]:
#          return False
#      return is_palindrome(a[start+1:end])
#
# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))
# print(is_palindrome("level"))

# def ftail(n,acc=1):
#     if n==0 or n==1:
#         return acc
#     return ftail(n-1,n*acc)
# print(ftail(4))

# def ackerman(m,n):
#     if m==0:
#         return n+1
#     elif m>0 and n==0:
#         return ackerman(m-1,1)
#     else:
#         return ackerman(m-1,ackerman(m,n-1))
# print(ackerman(2,1 ))

# def func(n):
#     if n>50:
#         return n-5
#     else:
#         return func(n+5)
#
# print(func(29))


# def sfact(n):
#     if n<=0:
#         return 1
#     return fact(n)*fact(n-1)
# def fact(n):
#     if n<=1:
#         return 1
#     return n*fact(n-1)
# print(sfact(5))
# print(sfact(4))


def pt(a,n):
    if n==1:
        return a
    return a**pt(a,n-1)

print(pt(2,3))
print(pt(3,2))