#!/usr/bin/env python
# coding: utf-8

# Question 1

# In[2]:


marks = {'Andy':88, 'Amy':66, 'James':90, 'Jules':55, 'Arthur':77}


# Q1.1

# In[3]:


def findGrade(student_name):
    if student_name in marks:
        print(marks[student_name])
    else:
        print('Cannot find', student_name)

findGrade("Amy")
findGrade("James")
findGrade("John")


# Q1.2

# In[4]:


def aveGrade():
    total = 0
    for student_name in marks:
        total += marks[student_name]
    ave = total/len(marks)
    return ave

aveGrade()


# Question 2

# In[5]:


def printSquare(num):
    n = 0
    while n <= num:
        print(n, n**2)
        n += 1
    else:
        print('Greater than', num)

printSquare(8)


# Question 3

# In[6]:


def add_all(num):
    n = 1
    total = 0
    while n <= num:
        total += n
        n += 1
    print(total)

add_all(5)


# Question 4

# In[7]:


def add_all_step(num):
    total = 0
    for i in range(1, num+1):
        total += i
        print(total)

add_all_step(5)


# Question 5

# In[8]:


import statistics
list1 = list(range(1,100))


# In[9]:


def calc_stats(list1):
    print('Mean:', statistics.mean(list1))
    print('Sum:', sum(list1))
    print('Standard Deviation', statistics.stdev(list1))

calc_stats(list1)


# Question 6

# Q6.1

# In[10]:


def minimal(v1,v2,v3,v4):
    if v1 <= v2 and v1 <= v3 and v1 <= v4:
        return v1
    elif v2 <= v3 and v2 <= v4:
        return v2
    elif v3 <= v4:
        return v3
    else:
        return v4

minimal(1,2,3,4)


# Q6.2

# In[11]:


def print_minimal(v1,v2,v3,v4):
    print(minimal(v1,v2,v3,v4))

print_minimal(2,4,5,0)
print_minimal(2,3,2,10)


# In[ ]:




