"""
any string = "  "

I: I have AAA cats and BBB dogs
          ^

Output; I have 3A cats and 3B dogs

Input: Today we will DD go to the beach, then FFFF to the mall
Output: Today we will 2D go to the beach, then 4F to the mall

uppercase

repeating characters



i have an aardvark
i have an 2ardvark

compression algorithm

uppercase

text1 DDE text2

2DE


split(' ')

traverse 
look for uppercase regex to get only uppercase

freq_map[] I, 1
   A,3
   B,3


I have 3A cats and 3B dogs

A super AA


"""
from collections import defaultdict 

input_str ="I have AAA cats and BBB dogs"
output=""
#freq map
freq=defaultdict(int)

for letter in input_str:
	if letter.isupper():
		if letter not in freq:
			freq[letter] = 1
		else:
			freq[letter] = freq[letter] + 1
			
print(freq)
freq=defaultdict(int)
for letter in input_str:
        if letter.isupper():
            freq[letter] += 1

print(freq) 
"""
 consecutive repeating characters Compression
input_str ="I have AAA cats and BBB dogs"
                   ^
                   cont= 2
                   till no more duplicated char 


"""

input_str ="Today we will DD go to the beach, then FFFF to the mall"
 
def encode(input_str)->str:
	ret = [] 
	i = 0
	while i < len(input_str):
		cont = 1
		while (i+1) < len(input_str) and input_str[i].isupper() and input_str[i] == input_str[i+1]:
			cont+=1
			i+=1
		if cont == 1:
			ret.append(input_str[i])
		else:
			ret.append(str(cont))
			ret.append(input_str[i])		
		i+=1
	return "".join(ret)

print(encode(input_str))


assert encode("D D D Hello") == "D D D Hello"
assert encode("DD") == "2D"
assert encode("Dd") == "Dd"
assert encode("DDDDD") == "5D"
assert encode("I have AAA cats and BBB dogs") == "I have 3A cats and 3B dogs"
assert encode("AAA and BBB") == "3A and 3B"
assert encode("A super BBB A") == "A super 3B A" 
assert encode("Today we will DD go to the beach, then FFFF to the mall") == "Today we will 2D go to the beach, then 4F to the mall" 
print("All assertions passed")













