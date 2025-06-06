"""
Alice has a binary string. She thinks a binary string is beautiful 
if and only if it doesn't contain the substring “010”. In one step, 
Alice can change a 0 to a 1 or vice versa. 

Count and print the minimum number of steps needed to make Alice see the string as beautiful.

b = 010
She can change any one element and have a beautiful string.

000

000000

Sample Output 0
2 
Explanation 0:
In this sample, b = '0101010'
The figure below shows a way to get rid of each instance of ‘010’:
0101010 ->
 0 0 0^
^
      ^

0111010 ->
  ^  ^  
0111000
100
010

010

01010

search for overlapping 01010 => 

0101001010
         ^
0111001110



0101010
   ^
0111010
      ^
  11011        
           



how many bits flipped?
overlapping

0101010 ->


0111010 ->

0111000



                 *
                 010
            /
            *        \\ *
           110        `         010 
          /    \\             /          \\
          100   110         000         010





Make the string beautiful by changing 2 characters (b[2] and b[5]).

0101010
 0 0 0^

0110010
 ^ 
 0
0101010
     ^

"""
def is_beautiful(s):
    l = 0
    ops =0
    #while (l <= len(s) -3):
    for l in range(len(s) - 2):
        window = s[l:l+3]
        #print(f"window: {window}")
        if window == "010":
            #s[l:l+3] = "011" #string immutable
            #s = s[:l] + "011" + s[l+3:]
            s = s[:l+2] + "1" + s[l+3:]
            l+=3
            ops+=1
    #   l+=1
   # print(f"string: {s}, ops: {ops}")
    return ops, s

assert is_beautiful("0101010") == (2, "0111011")
print("all assertions passed")




"""
HackerRank Problem: Beautiful String
1. Beautiful String
A string is beautiful if no two adjacent characters are either
1. the same, for example 'aa'.
2. adjacent in the alphabet, for example 'ef'.
The following operations can be performed on a string, s.
·
Choose any index i (0 ≤ i< |s|) and change s[i] to any lowercase English letter.
Find the minimum number of operations required to make the string beautiful.
Example
s="abdde"
String s is not beautiful because:
• 'dd' violates constraint 1, no two adjacent characters are the same.
• 'ab' and 'de' violate constraint 2, no two adjacent characters are adjacent in the alphabet.
The string can be converted into a beautiful string after 2 operations. One solution is below.
• Choose 1 and change s[i] to 'z'. s becomes "azdde".
• Choose -3 and change s[i] to 'k'. s becomes "azdke" which is beautiful.
Note: There are many other solutions such as "ardze", "axdke", etc.
It can be shown that 2 is the minimum number of operations required so return 2.
Function Description
Complete the function getMinimum OperationCount in the editor below.
getMinimumOperationCount has the following parameter:
s: a string
Returns
int: the minimum number of operations required to make s beautiful
"""

def getMinimumOperationCount(s: str) -> int:
    operations = 0
    n = len(s)

    for i in range(1, n):
        prev = s[i - 1]
        curr = s[i]

        # Check for same character or consecutive in alphabet
        if curr == prev or abs(ord(curr) - ord(prev)) == 1:
            operations += 1
            # Simulate a change: skip the current character in future comparisons
            # by setting it to a dummy value that won't match next char
            s = s[:i] + '#' + s[i+1:]

    return operations

assert getMinimumOperationCount("abdde") == 2
assert getMinimumOperationCount("bcbb") == 2
print("all assertions passed 2")




