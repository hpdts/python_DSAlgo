from itertools import product

def say_hello():
    print('Hello, World')

"""
for i in range(5):
    say_hello()
"""
# contains appears on the number 51 divisible by 5, cats
# contains 7 div 7 boots
#35 divisible when number is cats and boots you return both strings
# "boots and cats"  

def game_academia(num:int):
    #for num in range(n):
    if (contains_number(num, 5) or num % 5 == 0) and (contains_number(num, 7) or num % 7 == 0):
        return "boots and cats"
    if contains_number(num, 5) or num % 5 == 0:
        return "cats"
    elif contains_number(num, 7) or num % 7 == 0:
        return "boots"
    return num

def contains_number(num:int, contained_num:int):

    if str(contained_num) in str(num):
        return True
    else:
        return False

print("All assertions passed.")
"""
# 35 , 5 , 7 , 8
print(game_academia(5))
print(game_academia(7))
print(game_academia(51))
print(game_academia(50))
print(game_academia(21))
print(game_academia(1))
print(game_academia(28))
print(game_academia(23))
print(game_academia(35))
print(game_academia(70))
print(game_academia(72))"
"""

# div5 cont5 div7 cont7 numbers
#   √    √     x    x   5, 15, 25: 5
#   √    √     T    x   5, 15, 25
#   √    x     x    x   10, 20, 30
#   x    x     x    x   1,2,3,4,6:1
# 16 if reproduce booleans
# dict : div,5, cont,5 
# fill up the dict with teh number_of_conditions
# execute the dict with any conditions
# produce or print a set of numbers:  16 numbers:  [1...357]
# div5,div7

# 1   5  
# 1
#print("conditions")
def find_number_set_condition(conditions: list)->int:
    number_conditions = len(conditions) 
    #print(number_conditions)
    candidate = 1
    while number_conditions:
        for condition in conditions:
            op, num = condition[0], condition[1]
            #print(f"op: {op}, num: {num}, number_conditions: {number_conditions}")
            if op == "div" and candidate % num == 0:
                number_conditions-=1
            elif op == "cont" and contains_number(candidate, num):
                number_conditions-=1
            else:
                number_conditions = len(conditions) 
                break
        if number_conditions == 0:
            return candidate
        candidate+=1

assert find_number_set_condition([["div", 5], ["div", 7]]) == 35, "Test failed for conditions [['div', 5], ['div', 7]]"
assert find_number_set_condition([["div", 5]]) == 5, "Test failed for conditions [['div', 5]]"
assert find_number_set_condition([["cont", 60], ["div", 5]]) == 60, "Test failed for conditions [['cont', 60], ['div', 5]]"

print("All assertions passed.")

def generate_conditions_map(conditions: list):
    condition_types = ["div", "cont"]
    all_combinations = list(product(condition_types, repeat=len(conditions)))
    print(all_combinations)
    conditions_list = []

    for combination in all_combinations:
        condition_set = [[combination[i], conditions[i]] for i in range(len(conditions))]
        conditions_list.append(condition_set)

    return conditions_list

# Example usage
conditions = [5, 7]
conditions_list = generate_conditions_map(conditions)

#print(conditions_list)
#find_number_set_condition(conditions_list)

#minimun_common_divisor
# lowest number to do all false is 1
#lowest number to each condition
# ...
#...
# how many rows in this table?
# div5
#   F    1,2,3,4
#   T    5,10,
# 2 rows

# div5  cont5
#   F     F
#   F     T
#   T     F
#   T     T
# 4 rows

#  div5  cont5  div7
# ... 8 rows

# 2^number_of_conditions  == 16

