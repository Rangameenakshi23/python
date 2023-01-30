#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
user=input("Enter your choice:")
arr=["rock","paper","scissors"]
computer=random.choice(arr)
print(" choosen by computer:",computer," choosen by user:",user)
if(user=="rock" and computer=="scissors"):
  print("user won")
elif(user==computer):
  print("DRAW MATCH")
elif(user=="paper" and computer=="rock"):
  print("user won")
elif(user=="scissors" and computer=="paper"):
  print("user won")
else:
  print("computer won")


# In[12]:


from random import randint 
arr=['rock','paper','scissor']
ppoint=0
cpoint=0
for i in range(0,5):
    player=input()
    com = arr[randint(0,2)]
    print("computer choose",com)
    if player==com:
        print("play again") 
    if ((player=='rock')&(com=='paper')):
        print("com win")
        cpoint=cpoint+1
    if ((player=='paper')&(com=='rock')):
        print("player win")
        ppoint=ppoint+1
    if ((player=='scissor')&(com=='paper')):
        print("player win")
        ppoint=ppoint+1
    if ((player=='paper')&(com=='scissor')):
        print("com  win")
        cpoint=cpoint+1
    if ((player=='scissor')&(com=='rock')):
        print("com win")
        cpoint=cpoint+1
    if ((player=='rock')&(com=='scissor')):
        print("player win")
        ppoint=ppoint+1
if(ppoint==cpoint):
    print("draw match")
elif(ppoint<cpoint):
    print("computer win",cpoint,"player points",ppoint)
else:
    print("player win",ppoint,"computer points",cpoint)


# In[ ]:




