#!/usr/bin/env python
# coding: utf-8

# In[1]:


def happy(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
num=97
result=num
while(result!=1 and result!=4):
    result=happy(result)
    if result==1:
        print("happy number")
    else:
        print("not happy number")


# In[7]:


#given a maximum of 4 digit to the base17 10-A,11-B,12-C,......16-G as input ,output its decimal value.
#test cases 1.input-1A ,expected output-27 2.input-23GF expected output-10980
num=str(input())
print(int(num,17))
num=str(input())
print(int(num,17))


# In[10]:


#Harshed number
#num=189,this number should be exactly divisible by its sum
num=189 
sum=1+8+9
num=num%sum
if num%sum==0:
    print("the num is exactly divided")
else:
     print("the num not is exactly divided")


# In[11]:


#write a program to convert f to c
fa=float(input("enter the value"))
ce=(0.58)*(fa-32)
print(ce)


# In[16]:


#write a program to check whether the given number is positive or negative
num=int(input("enter the value"))
if num>0:
    num=num+10
    print(num)
    print("the num is positive")
else:
    print("the num is negative")


# In[17]:


#write a program to determine the char entered 2.palindrom 3.symmetric 4.anactromes
#write a program to find a txt present in the sentence or not
txt="Telangana is a state"
if "Telangana" in txt:
    print("present")
else:
    print("not present")


# In[24]:


#write a program to  remove all the s's from the word MISSISSIPPI  and print the remaining letters in the word
a="MISSISSIPI"
print(a.split("S"))


# In[25]:


a.upper()


# In[26]:


a.lower()


# In[35]:


a[::-1] 


# In[31]:


#string access indexng
abc='netherlands'
print(abc[1])


# In[36]:


#string access indexng slice
abc='netherlands'
print(abc[1:4])
abc[::-1]


# In[37]:


#string multi-line
abc="""
netherlands
usa
uk"""
print(abc)


# In[41]:


#string comparision
abc='hi'
abc1='hello'
abc2='hi'
print(abc==abc1)
print(abc==abc2)
print(abc+abc1)


# In[46]:


#int swaping
#x,y=y,x
#a=t,b=a,t=b
#a=a+b,b=a-b,a=a-b
#a=a*b,b=a/b,a=a/b
#a=a^b,b=a^b,a=a^b
#string length by using method sum
def ls(string):
    return sum(1 for i in string)
string="india"
print(ls(string))

#string length by using method counter
def ls(str):
    c=0
    for i in str:#while str[c:]
        c+=1
    return c
str="sru"
print(ls(str))

#string length by using join and count
def ls(str)
  if not str:
        return 0
else:
    r_str='Mr'
    return((r_str).join(str).c(r_str)+1)
str="uae"
print(ls(str))
    


# In[50]:


name='meenakshi'
country='india'
print(f'{name} is born in {country}')


# In[ ]:


#sets
m_set={1,2,3}


# In[51]:


x={}
print(type(x))
y=set()
print(type(y))


# In[54]:


#modifying set
m_set={1,3}
m_set.add(2)
print(ls(str))
m_set.update([2,3,4])
print(m_set)
m_set.update([4,5],{1,6,7})
print(m_set)


# In[57]:


my_set=set("happy")
print(my_set)
print(my_set.pop())
print(my_set)


# In[59]:


#there is a jar full of candies for sale at a mall counter.jar has the capacity n,that is jar can contain maximum N candies when jar is full .At any point of time.Jar can have m number of candies where M<=n.candies are served to the customers.jar is never remain empty as when last k candies are left.Jar is refilled with new candies in such a way that Jar get full
#write a code to implement above scenario.display jar at counter with available number of candies.Input should be number of canies one customer can oederat point   of time.Updtaethe jar after each purchase and dispaly jar at counter.
#if input is more than candies in jar,return :"INVALID INPUT"given,
#N=10,where N is number od candies available
#k<=5,where k is number of minimum candies that must be inside jar ever.
#example 1:n=10,k=<5
#input value 3
#output value:number of candies sold:3   ,number of candies available:7
totalcandies = 10
candies = int(input())
if candies in range(1, 6):
    print('No. of Candies Sold:',candies)
    print('No. of Candies available:',totalcandies-candies)
else:
    print("Invalid Input")
    print('No. of Candies available:',totalcandies)


# In[66]:


#A digital machine generates binary data which consists of a string of 0s and 1s .A maximum signal M,in the data ,consists of the maximum number of either 1s and 0s apperring consecutively in the data but m can't be at the beginning or end of the string .Design a way to find the length of the maximum signal.
#input
#the first lie of input consists of an integer N,representing the length of the binay string.
#the second line consists of a string of length N consisting of 0s and 1s only.
#output
#print an integer representig the length of maximum signal 
#input
#6
#101000
#output
#1
#explanation for 101000,M can be 0 at the second index or at the third index so tin both cases max length=1
#example 2
#input
#9
#101111110
#output
#6
a=int(input())
max=0
count=0
flag=0
binary=input("enter the binary value")#we r taking the string of the binary are combine dtogether
arr=list(binary) #arranging the the binary in the list format
for i in range(0,a):
        if arr[i]=='1':#if the 1 is occuring then the count is increased by1
           count=count+1
           flag=1
        elif(arr[i]=='0' and flag==1):#if the index arranged as 0 then the count is equal to 0 
           count=0
           flag=0
        if count>max:
           max=count
print(max)
        
        


# In[ ]:




