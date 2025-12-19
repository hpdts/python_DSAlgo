#!/bin/python3

import math
import os
import random
import re
import sys

"""
Intervals
no overlapping
0-24



while curr < end:
8 10    - 17
^
  js

ret = []
if js < is
   ret.append(js, is)
   js= ie 



8,9



ret= 8,9  -  10,11


[(9,10)(11,12)(14,15)]
  ^
 is.ie
 

opens = 9
[(9,11)(11,12)(14,15)]
                   ^
"""
def availableTimeSlots(appointments, startTime, endTime):
    """
    This function calculates the available time slots between appointments.

    :param appointments: List of tuples, where each tuple contains two integers representing the start and end times of an appointment.
    :param startTime: Integer representing the clinic's opening time in 24-hour format (e.g., 8 for 8:00 AM).
    :param endTime: Integer representing the clinic's closing time in 24-hour format (e.g., 17 for 5:00 PM).
    :return: List of tuples, where each tuple contains two integers representing the available time slots between appointments.
    """
    # TODO: Implement the function logic here
    #pass
    start = startTime
    end = endTime
    ret = []
    
    for apt_start,apt_end in appointments:
        if start < apt_start:
            ret.append((start, apt_start))
            start = apt_end 
        elif start == apt_start:
            start = apt_end 
    
    if start < end:
        ret.append((start, end))
    
    return ret
    

assert availableTimeSlots([(9, 10), (11, 12), (14, 15)], 8, 17) == [(8, 9), (10, 11), (12, 14), (15, 17)]
assert availableTimeSlots([(8, 9), (12, 13), (16, 17)], 8, 17) == [(9, 12), (13, 16)]
assert availableTimeSlots([], 8, 17) == [(8, 17)]
print("All test cases pass")