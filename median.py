# import requests
# import mysql.connector
# import pandas as pd

# median of a stream of input
# consume(input)
# calculate() -> 


"""
int input


Median

no sorted


123 
 ^
 
12

3/2 = 1.5

sort the data
calculate the median 


1

median = 1


13

median = 2

consume(1)
consume(2)
calculate() -> 1.5
consume(3)
calculate() -> 2

n space
append data to a list
sort and  get median
nlog(n)

data structurte that can do better

12345 
  ^
16 bits integers

counter = 23
smaller= min(smaller, )
bigger=

counter = 4
4/2 = 2
(4/2)-1

0 1,2 ...99
1,2,3,....100
 
if counter % 2 != 0:
  get the one in tne middle
else:
  // get the middle and middle -1 / 2
  
2^16
0001000.....

0 + counter
index:0123
      0101



onkly integers and we need to find then ones in ghe middle

insertion sort

       consume(10)
       comsume(2)
       
       
      1,2,56,100
      ^
 BST     
     

  
  
1234 = 2.5  

min heap  the smallest number

not duplication
"""
buffer = [0] * 1000

#1000 binary

count = 0


def consume(number):
  buffer[number] = 1
  count+=1


def calculate():
  mid_index = counter / 2
  if counter % 2 != 0:
    # get the one in tne middle
    return buffer[mid_index]
  else:
    # get the middle and middle -1 / 2
    mid_index_prev = mid_index -1
    return (buffer[mid_index_prev] + buffer[mid_index]) / 2
    

consume(1)
consume(2)
print(calculate())


#print('Hello')
