#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'vowelsubstring' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts STRING s as parameter.
#
# sliding window 5 vowels
# just need to check one vowel on the substring
# get all substring 
from collections import Counter

def contains_vowel_once(s):
    freq = Counter(s)
    vowels = set()
    vowels.add('a')
    vowels.add('e')
    vowels.add('i')
    vowels.add('o')
    vowels.add('u')
    for key, val in freq.items():
       # print(f"key: {key}, val:{val}")
        if key in vowels:
            vowels.remove(key)
    
    return True if len(vowels) == 0 else False
    
def vowelsubstring2(s):
    # Write your code here
    ret = 0
    seen = set()
    for sub_index1 in range(0, len(s)):
        for sub_index2 in range(sub_index1+1, len(s)):
            sub_string = s[sub_index1:sub_index2]
            print(f"sub_string: {sub_string}")
            if sub_string not in seen and contains_vowel_once(sub_string):
                ret+=1
                seen.add(sub_string)
                
            #if sub_string == 'aeiou':
            #   ret+=1
            
    return ret

def all_vowels(vowel_count):
    for count in vowel_count:
        if count == 0:
            return False
    return True


def vowelsubstring(s):
    n = len(s)
    ret = []
    
    for i in range(n):
        vowel_count = [0] * 5
        curr = ""
        for j in range(i, n):
            ch = s[j]
            #print(f"ch: {ch}")
            if ch not in 'aeiou':
                break
            curr+=ch
            if ch == 'a':
                vowel_count[0]+=1
            if ch == 'e':
                vowel_count[1]+=1
            if ch == 'i':
                vowel_count[2]+=1
            if ch == 'o':
                vowel_count[3]+=1
            if ch == 'u':
                vowel_count[4]+=1

            if all_vowels(vowel_count):
                ret.append(curr);
    print(f"ret: {ret}")
    return len(ret)



def test_vowelsubstring():
    # Test Case 1: All vowels in order
    s = "aeiou"
    result = vowelsubstring(s)
    assert result == 1, f"Test Case 1 Failed: {result}"  # Only one substring contains all vowels

    s = "aaeiouxa"
    result = vowelsubstring(s)
    assert result == 2, f"Test Case 1 Failed: {result}"  # Only one substring contains all vowels

    """
    # Test Case 2: All vowels repeated
    s = "aeiouaeiou"
    result = vowelsubstring(s)
    assert result == 15, f"Test Case 2 Failed: {result}"  # Multiple substrings contain all vowels
    
    # Test Case 3: Mixed characters with vowels
    s = "abcdeiouxyz"
    result = vowelsubstring(s)
    assert result == 1, f"Test Case 3 Failed: {result}"  # Only one substring contains all vowels

    # Test Case 4: No vowels
    s = "bcdfghjklmnpqrstvwxyz"
    result = vowelsubstring(s)
    assert result == 0, f"Test Case 4 Failed: {result}"  # No substring contains all vowels

    # Test Case 5: Single vowel
    s = "a"
    result = vowelsubstring(s)
    assert result == 0, f"Test Case 5 Failed: {result}"  # Not enough vowels to form a valid substring

    # Test Case 6: Empty string
    s = ""
    result = vowelsubstring(s)
    assert result == 0, f"Test Case 6 Failed: {result}"  # No substrings possible

    # Test Case 7: Overlapping substrings
    s = "aeiouaeiouxyz"
    result = vowelsubstring(s)
    assert result == 15, f"Test Case 7 Failed: {result}"  # Multiple substrings contain all vowels

    # Test Case 8: Random characters with vowels
    s = "aebcdiouxyz"
    result = vowelsubstring(s)
    assert result == 1, f"Test Case 8 Failed: {result}"  # Only one substring contains all vowels

    """

    print("All test cases passed!")


# Run the tests
test_vowelsubstring()

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = vowelsubstring(s)

    fptr.write(str(result) + '\n')

    fptr.close()
"""