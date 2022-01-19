#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a function that takes a list of lists and returns the value of all of the
#symbols in it, where each symbol adds or takes something from the total
#score.
    
def check_score(l):
    d={'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
    a=0
    b=0
    if type(l)==list:
        for i in l:
            for j in i:
                for key,value in d.items():
                    if j==key:
                        a=value
                        b=b+a
    if b>0:
        return b
    else:
        return 0
                                          
                


# In[2]:


check_score([['#','!'],['!!','X']])


# In[3]:


check_score([['!!!','O','!'],['X','#','!!!'],['!!','X','O']])


# In[4]:


#Create a function that takes a string as an argument and returns the Morse
#code equivalent.

char_to_dots = {
'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '': '', '0': '-----',
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
'&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
'-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
    
def encode_morse(*args):
    b=[]
    for i in args:
        for key, value in char_to_dots.items():
            for j in i:
                if j in char_to_dots:
                    b.append(char_to_dots[j])
                    
                    
            return " ".join(b)                    


# In[5]:


encode_morse("HELP ME !")


# In[6]:


d={'a':1,'b':2,'c':3, 'd':4,'e':5, 'f':6, 'g':7, 'h':8, 'i':9,'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 
   'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23,'x':24, 'y':25, 'z':26}
def to_boolean_list(*args):
    b=[]
    a=[]
    for i in args:
        for key, value in d.items():
            for j in i:
                if j in d:
                    if d[j]%2==0:
                        b.append(0)
                    else:
                        b.append(1)
            for k in b:
                if k==0:
                    a.append(False)
                else:
                    a.append(True)
            return a
                


# In[7]:


to_boolean_list("deep")


# In[8]:


#2. Create a function that takes a variable number of arguments, each
#argument representing the number of items in a group, and returns the
#number of permutations (combinations) of items that you could get by taking
#one item from each group.


def combinations(*args):
    b=1
    for i in args:
        b=b*i
    return b    
        


# In[9]:


combinations(2,3,4,5)


# In[21]:


#Write a function that takes a number and returns True if it&#39;s a prime; False
#otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With
#the standard technique it would be O(2^64-1), which is much too large for the
#10 second time limit.

def prime(num):
    flag=True
    if num>1:   
        for i in range(2,int(num)):
                if num % i==0:
                    flag=False
                break
        
    return flag


# In[24]:


prime(7)


# In[ ]:




