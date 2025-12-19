#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximizeCPU' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY requirements
#  2. INTEGER processingCapacity
#

"""
[15,12,3,7,8]


max= <=maxCapacity
n = 0
n =1
i=n
n=2

15


[7,6,9,11]
     
 
   
25


level = 1
Recursion
 0 1 2
[2,9,7]
     i 
 
 
"""
def sum_group(group):
    print(f"group: {group}")
    tot = 0
    for num in group:
        tot+=num
        
    return tot

def get_groups_wrong(requirements, processingCapacity, groups, level):
    ret = -1
    for index,num in enumerate(requirements):
        print(f"index: {index}, num: {num}, level: {level}")
        sum_withinCap = sum_group(requirements[index:level])
        ret = max(sum_withinCap, ret)
        """
        j = index + level
        while j < len(requirements):
            print(f"j: {j}, requirements[index:j]: {requirements[index:j]}")
            sum_withinCap = sum_group(requirements[index:j])
            ret = max(sum_withinCap, ret)
            j+=level
        """
    return ret

def get_groups(requirements, processingCapacity, level):
    ret = -1
    print(f"level: {level}")
    for i in range(len(requirements) - level + 1):
        window = requirements[i:i+level]
        s = sum(window)
        print(f"index: {i}, window: {window}, sum={s}")
        if s <= processingCapacity:
            ret = max(ret, s)
    return ret
    

def maximizeCPU(requirements, processingCapacity):
    # Write your code here
    print(f"requirements: {requirements}, processingCapacity: {processingCapacity}")
    ret = -1
    for level in range(1,len(requirements)+1):
        max_withinMaxCap = get_groups(requirements, processingCapacity, level)
        ret = max(max_withinMaxCap, ret)
    
    return ret

def maximizeCPU_subset(requirements, processingCapacity):
    ret = []
    m = float('-inf')

    def get_groups_subset(build, depth):
        if depth == len(requirements):
            ret.append(build[:])
            return

        get_groups_subset(build, depth + 1)
        get_groups_subset(build + [requirements[depth]], depth + 1)

    get_groups_subset([], 0)
    for group in ret:
        s = sum(group)
        if s <= processingCapacity:
            m = max(s, m)
    return m

print(maximizeCPU_subset([2,9,7], 25))

assert maximizeCPU_subset([2,9,7], 25) == 18
assert maximizeCPU([2,9,7], 25) == 18
assert maximizeCPU([2,9,7], 17) == 16
assert maximizeCPU([15,12,3,7,8], 18) == 18
print("all assertions passed")