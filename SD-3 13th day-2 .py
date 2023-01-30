#!/usr/bin/env python
# coding: utf-8

# In[1]:


#looping statements
i=0
while(i<=10):
  print(i)
  i+=1


# In[2]:


#looping statements,to print the numbers in a row
i=0
while(i<=10):
  print(i,end=" ")
  i+=1


# In[3]:


i=0
while(i<=10):
  print(i,end="\t")#\t is the tab space
  i+=1


# In[4]:


#write a program to add elements between a range of m,n where m=3,n=9
m=3
n=9
sum=0
while(m<=n):
    sum=sum+m
    m=m+1
    print(sum)


# In[5]:


#write a program to find sum of the digist in a number
sum=0
num=123
while(num!=0):
        rem=num%10
        sum=sum+(rem)
        num=num//10
print(sum)


# In[6]:


#write a program to reverse of a number with the space provided btw them
num=123
rem=0
sum=0
temp=num
while(num>0):
        rem=num%10
        num=num//10
        print(rem,end=" ")
        
#write a program to reverse of a number with the space provided btw them
num=1234
n_string=str(num)
r_num="".join(reversed(n_string))
print(r_num,end=" ")

#write a program to reverse of a number with the space provided btw them
def reverse(n):  
    if len(n)==0:
        return n
    return reverse(n[1:])+n[0] 
num=1234
n_string=str(num)
r_num=reverse(n_string)
print(r_num,end=" ")


# In[7]:


#program to calulate thr first n numbers  average
n=int(input("enter the value of n"))
avg=0.0
s=0
for i in range(1,n+1):
    s=s+i
avg=s/i
print(s)
print(avg)


# In[8]:


#program of multipilaction  of a table
n=int(input("enter the value of n"))
for i in range (1,11):
    print(n,"×",i,"=",n*i)
    


# In[9]:


#program to print leap years in adjacent
m=1900
n=2101
for i in range(1900,2101):
    if i%4==0:
        print(i,end=" ")


# In[10]:


#program to find sum of geometric series
n=int(input("enter the value of n"))
s=0.0
for i in range(1,n+1):
    a=1.0/i
    s=s+a
print(str(s))


# In[11]:


#program to find sum of geometric series where the with the denominator with squares
n=int(input("enter the value of n"))
s=0.0
for i in range(1,n+1):
    a=1.0/i
    # a=1.0/(i**2)
    s=s+a*a
print(str(s))


# In[12]:


#strings
str="hi"
print(str.capitalize())


# In[13]:


str="hello"
print(str.center(10,'$'))
str="hi"
print(str.center(10,'$'))


# In[14]:


str="he"
substr="hehellhell"
print(substr.count(str,0,len(substr)))


# In[18]:


str="he is my cousin"
print(str.find("my",0,len(str)))


# In[19]:


#syntax for left justifications
#ljust -width[,fillchar]
str="hi"
print(str.rjust(20,'^'))


# In[22]:


#syntax for zfill-width
str="6"
print(str.zfill(4))


# In[27]:


str="the prometheus has a ship"
print(str.title())
print(str.swapcase())
print(list(enumerate(str)))


# In[29]:


str1="India has won"
for i in str1:
    print(i,end=" ")


# In[35]:


#caeser cipher
str="pakistan is in danger"
index=0
while index <len(str):
    letter=str[index]
    print(chr(ord(letter)+1), end=' ')
    index+=1
    
str="india"
index=0
while index <len(str):
    letter=str[index]
    print(chr(ord(letter)+2), end='')
    index+=1


# In[53]:


#Abecedarian series,patters,siphers,functions,passing parameters
str="ate"
l=['a','b','c']
str1=' '
for i in l:
    str1=i+str+' '
    print(str1)


# In[60]:



val=int(input("enter the position"))
a=b=0
for i in range(1,val+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if val%2!=0:
    print('{} at accordance {}'.format(val,a-7))
else:
    print('{} at accordance {}'.format(val,b-6))


# In[66]:


#find the nth term of the series.1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187......
#this series is a mixture of 2 series-all odd terms form a geometric 
#find 13th position
#find 16th position

num=int(input("enter the position"))
if(num%2==0):
    num=num//2
    print(3**(num-1))
else:
    num=num // 2+1
    print(2**(num-1))


# In[ ]:





# In[ ]:




