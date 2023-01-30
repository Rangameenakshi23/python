#!/usr/bin/env python
# coding: utf-8

# In[11]:


str1="abcdefgh"
str2="ate"
for letter in str1:
    print(letter +str2,end="  ")


# In[12]:


#-patterns
#-basic patterns
#-mirror image patterns
#-symmetrical patterns
#- chain of patterns
#-Anti-patterns


# In[13]:


for i in range(1,5):
    for j in range(1,i+1):
         print(j,end="  ")
    print("\n")
    
#or
rows=int(input("enter the value of rows"))
for i in range(rows):
    for j in range(i+1):
         print(j+1,end="  ")
    print("\n")


# In[14]:


for i in range(1,5):
    for j in range(1,i+1):
         print("*",end="  ")
    print("\n")


# In[17]:


rows=int(input("enter the value of rows"))
for i in range(rows,0,-1):
    for j in range(0,i):
         print(j+1,end="  ")
    print("\n")


# In[18]:


rows=int(input("enter the value of rows"))
ch=input()
for i in range(1,rows +1):
    for j in range(1,rows+i):
        if (j<i):
             print('',end="  ")
        else:
             print('%ch'%ch,end="  ")
    print(" ")
    


# In[19]:


rows=int(input("enter the value of rows"))
i=1
while(i<=rows):
    j=1
    while(j<=rows):
        if j<i:
            print(' ',end=' ')
        else:
            print('@',end=' ')
        j=j+1
    i=i+1
    print()
 


# In[22]:


n=int(input())
for i in range(n, 0, -1):
  for j in range(0, i):
    print(" ", end=" ")
  for n in range(i, n+1 ):
    print(n, end=' ')
  print()


# In[20]:


#diamond or rhombus pattern
rows=int(input("enter the number="))
i=1
while i<=rows:
  j=rows
  while j>i:
    print(' ',end=' ')
    j-=1
  print('*', end=" ")
  k=1
  while k<2*(i-1):
    print(' ',end=' ')
    k+=1
  if i==1:
    print()
  else:
    print('*')
  i+=1
i=rows-1
while i>=1:
  j=rows
  while j>i:
    print(' ',end=' ')
    j-=1
  print('*',end=" ")
  k=1
  while k<2*(i-1):
    print(' ',end=" ")
    k+=1
  if i==1:
    print()
  else:
    print('*')
  i-=1


# In[10]:


row=5
k=2*rows-2
for i in range(0,rows):
  for j in range(0,k):
    print(end=" ")
  k=k-1
  for j in range(0,i+1):
    print("* ",end="")
  print("")
k=rows-2
for i in range(rows, -1, -1):
  for j in range(k, 0, -1):
    print(end=" ")
  k=k+1
  for j in range(0,i+1):
    print("* ",end="")
  print("")


# In[9]:


word="california"
x=""
for i in word:
    x+=i
    print(x)


# In[25]:


a=65
r=7
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch,end=" ")
        a+=1
    print(" ")


# In[54]:


a=65
r=5
m=(2*a)-2
for i in range(0, r):
    for j in range(0, m):
        print(end=" ")
    m=m-1
    for j in range(0, i+1):
        ch=chr(a)
        print(ch, end='')
        a+=1
    print(" ")


# In[56]:


rows=10
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i*j,end=" ")
    print()


# In[58]:


'''def username(arg1,arg2,arg3.........n):
    ----------
    ----------
    return'''#call by value
def diff(a,b):
    return a-b
x=20
y=10
operation=diff
print(operation(x,y))


# In[63]:


#program to dispaly a string n number of times
def fun():
    for i in range(5):
        print("hi students")
fun()


# In[65]:


def diff(a,b):#call by itself 
    result= a-b
    print("difference",result)
a=20
b=10
diff(a,b)


# In[66]:


#to speed up his composition of generating unpredictable rhytms,bluebandit wants the list of prime numbers avaolable in a range of numbers .Can you helphim ot?
#write a python program to pribt all prime numbers in the interval[a,b]
#Input 1 should be lesser than Input 2 both the inputs should be 'positive
#range must always be greater than zero.
#if any of the condition fails then display "provid valid input"
#use minimum of one for loop and one while loop
a=int(input("enter input1:"))
b=int(input("enter input2:"))
if(a<=0 or b<=0 or a>b):
    print("Enter valid input: ")
else:
    while(a<=b):
        if(a==2):
            print(a,end=" ")
        elif(a==1):
            a=a+1 
            continue
        else:
            flag=0 
            for i in range(2,a//2+1):
                if a%i==0:
                    flag=1 
                    break
            if(flag==0):
                print(a,end=" ")
        a=a+1 


# In[71]:


#x- pattern
n=int(input("enter the size"))
val=n*2-1
for i in range(1,val+1):
    for j in range(1,val+1):
        if i==j or j==val-i+1:
            print('*',end=" ")
        else:
            print('',end=" ")
    print()


# In[72]:


n=int(input("enter rows"))
for i in range(1,2*n):
    for j in range(1,2*n):
        if(i==n or j==n):
            print("*",end=" ") 
        else:
            print(" ",end=" ")
    print()


# In[74]:


#sand glass pattern
n=int(input("enter rows"))
for i in range(0,n):
    for j in range(0,i):
        print(end=" ") 
    for k in range(i,n):
            print("*",end=" ")
    print()
for i in range(size-1,-1,-1):
    for j in range(0,i):
        print(end=" ")
    for k in range(i,size):
        print("*",end=" ")
    print()


# In[ ]:


print("*",end=" ")

