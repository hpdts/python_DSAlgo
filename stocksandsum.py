# given predicted stock price for the next N days, write a function to return the max profit you can get by a single buy and then sell transaction.
    
# [10, 20, 15, 40], buy=10, sell=40, max profit = 30
#.         
#10, 5,40. max = 40
#-5, 20 
#25
#min_price = 10

"""
[10, 20, 15, 40]
 i
     j

  curr= 10
  next= 40
  10   5 
"""


# buyb amt min and sell at max


#min_price = min(curr_price, min_price)
#curr_profit = curr_price - min_price 
#max_profirt = max(curr_profit, max_profirt)

# 3 syntax errors
def sell_day(input):

    max_profit = 0
    for i in range(len(input)):
        for j in range(i+1,len(input)):
            curr_price = input[i]
            next_day_price=input[j]
            curr_profit = next_day_price - curr_price
            max_profit = max(max_profit, curr_profit)

    return max_profit

def sell_day2(input):
    min_price = float('inf')
    max_profit = 0

    for curr_price in input:
        min_price = min(curr_price, min_price)
        max_profit = max(max_profit, curr_price-min_price)

    return max_profit

assert sell_day([10, 20, 15, 40]) == 30
assert sell_day2([10, 20, 15, 40]) == 30
assert sell_day([7,1,5,3,6,4]) == 5
assert sell_day([7,6,4,3,1]) == 0


# 
#, what's the max profit you can get?
# [10, 20, 15, 40]
#.              ^
#.             ^
#  ^

#day 0 and sold on last day
#
#  1 stock per day, buy and sel diffreent days
# 10, 20 -> 10, 15,40->25, 10+25=35
# 10,40, 30


# 2. you are given two integers (string), write a function to return the sum of these two integers (result returned as string).
# "123", "19", -> "142"
 # 1
#321
#^
#91 
#^
#241

#12. // 10 = 1
#. 12 % 10 = 2

"""
321
   ^

91
   ^

f = 3 , 2
s = 9, 1
sum = 12
carry = 1
ret = 2

1 
9

"""
def sum_string(i1,i2):
    p1 = 0
    p2=0
    carryover = 0
    s1 = list(reversed(i1))
    s2 = list(reversed(i2))
    ret = []

    while p1 < len(s1) or p2 < len(s2):
        first_number = s1[p1] if p1<len(s1) else 0
        second_number = s2[p2] if p2<len(s2) else 0
        sum_number =  int(first_number) + int(second_number) + carryover
        result = sum_number % 10
        carryover = sum_number // 10
        ret.append(str(result))
        p1+=1
        p2+=1

    if carryover:
        ret.append(str(carryover))
    return "".join(reversed(ret))

assert sum_string("123", "19") == "142"
assert sum_string("11", "99") == "110"

#same sign +
#same sign negative we can * -1
#different sign 

# "11", "99"
#do substraction
# "-123", "19"
# "123", "-19"

"""
-123
   -19
=   

"""