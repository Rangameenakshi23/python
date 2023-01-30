#!/usr/bin/env python
# coding: utf-8

# #function -space is allocated in the memory location
# #function is in to patrs
# #fiunction header
# #funtion party
# syntax-def fun_name(var1,var2,.........):
#    documentation string
# statement block
# return[expression/value]
# no arguments-no return value
# example:
#     def fun():-------callee
#         for i in range(10):
#             print("abcde")
#     fun()---------------caller
# arguments passed with return values
# example:
#     def add(x,y):---function to add 2 numbers
#         return x+y
#     a=10
#     b=20
#     operstion=add----func name assigned to a variable
#     
#     print(operation(a,b))
#     
#     GLOBAL VARIABLE
#     it declares the local or the inner variable of the function to have module scope
#     

# In[3]:


#accessing global variable
var1="hi"
def abc():
    global var2
    var2="goodmorning"
    print("in the function var1 is -",var1)
abc()
print("outside the function var2 is -",var2)
print(" var1 is -",var1)


# In[6]:


#modifying global variable
var1="hi"
def abc():
    global var1
    var1="goodmorning"
    print("in the function var1 is -",var1)
abc()
print("outside the function var2 is -",var1)
var1="verygood"
print("outside the function after modiyfing is -",var1)


# In[8]:


#program to demonstrate access of var in inner and outer func
def outer_fun():#2
    outer_var=11#3
    def inner_fun():#6
        inner_var=22#7
        print("inner variable",inner_var)#8
    inner_fun()#5
    print("outer variable",outer_var)#4
outer_fun()#1


# In[10]:


#writing a function and return its cubation format
def cube(x):
    return (x*x*x)

num=10
result=cube(num)#cube(10)
print("cube of",num,"=",result)


# In[11]:


#writing a function to understand a mismatch parameters
def abc(x):
    print("hi students"+"×",x)
abc(5)


# In[13]:


def fun(i):
    print("orange",i)
j=10
fun(j)


# In[15]:


def fun(i):
    print("orange",i)
fun(5+2)


# In[25]:


#program to demo key args
def dispaly(str,int_x,float_y):
    print("the string is ",str)
    print("the integer is",int_x)
    print("the float is",float_y)
display(float_y=12345.6789,str="hi",int_x=1234)


# In[29]:


def display(name,age,salary):
    print("the name is ",name)
    print("the age is",age)
    print("the salary is",salary)
a="meenakshi"
b=20
c=100000000
display(name=a,age=b,salary=c)


# In[30]:


#lambda functions
addition=lambda x,y:x+y
print("sum=",addition(10,20))


# 1.lambda fun have no names
# 2.it can take n number of attributes
# 3.it can only return only one value
# 4.lambda func cannot access global variables
# 5.cannont access variables other than there parameters list
# 6.cannot contain nulti parameters
# 7.it doesn't have explict return statements

# In[31]:


#write a program to find smaller number by lamda
def small(a,b):
    if(a>b):
        return a
    else:
        return b
add = lambda x,y:x+y
diff = lambda x,y:x-y
print("smaller of two no=",small(add(-3,-2),diff(-1,2)))


# In[34]:


#program to pass a lambda of given parameters
def increment(y):
        return (lambda x : x+1)(y)
a=100
print("a=",a)
print("after incrementing")
b=increment(a)
print(b)


# In[36]:


#program to pass a lambda fun as an function arg
def fun(f,n):
    print(f(n))
twice = lambda x: x*2
triple=lambda x:x*3
fun(twice,4)
fun(triple,3)


# In[38]:


add=lambda x,y:x+y
m_and_add=lambda x,y,z:x*add(y,z)
print(m_and_add(3,4,5))


# In[39]:


x=lambda:sum(range(1,11))
print(x())


# In[43]:


#swap using functions
def swap(a,b):
    a,b=b,a
    print("after swap")
    print("a=",a)
    print("b=",b)
a=int(input("enter a="))
b=int(input("enter b="))
print("before swap")
print("a=",a)
print("b=",b)
swap(a,b)


# In[54]:


'''write a program to return the full name of a person where 1st variable passed is first name
2nd variable pased is last name'''
def person(a,b):
     e=' '
     n=a+e+b
     return n 
print(person("ranga","meenakshi"))


# In[57]:


def eo(n):
    if n%2==0:
        return 1
    else:
        return 0
n=int(input("enter the number"))
temp=eo(n)
if temp==1:
    print("the number is even")
else:
    print("the number is odd")


# In[64]:


#write a program to calculate SI.suppose the customer is a senoir citizen .He is being offered 12%ri,for all other customers,thri is 10%
def SI(age):
    if age>45:
        roi=12
        return 1
    else: 
        roi=10
        return 0
age=int(input("enter the age of the person"))
p=int(input("enter the principle amount"))
t=int(input("enter the time period in months"))
si=(p*t*roi)/100
if age>45:
    print("the age of the person is an senior citizen")
else:
    print("the age of the person is not a senior citizen")
    


# In[71]:


#factorial
def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
num=int(input("enter the number"))
print("the factorial of the given nuber is:",fact(num))


# In[85]:


#program to find the exp(x,y) using recurrsion function
def exp(x,y):
     if y == 0:
        return 1
     else:
        return (x*exp(x, y-1))
a = 5
b = 2
print(exp(a, b))


# In[88]:


#fibanocci series recursion
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("enter the number"))
for i in range(n):
    print("fibonaaci(",i,")=",fib(i))


# In[96]:


#towerof hanoi in recursion
def toh(n,a, b,c):
    if n==1:
        print("moving from tower present",a,"to which tower we should move reach",b)
        return
    toh(n-1,a,c,b)
    print(n,a, b)
    toh(n-1,c,b,a)
n=4
toh(n,'A','B','C')


# In[99]:


#towerof hanoi in iterative
def hanoi(n,a, b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if A:
            C.append(A.pop())
        hanoi(n-1,c,b,a)
A=[1,2,3,4]
B=[]
C=[]
print(A,B,C)
hanoi(A,B,C)


# In[ ]:




