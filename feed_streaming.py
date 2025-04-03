"""
cool string char same freq
"""
from collections import Counter 
def iscool(s):

	if not s:
		return True 

	freq = Counter(s)


	curr_freq = freq[s[0]]
	#print(f"curr_freq: {curr_freq}")

	for key, val in freq.items():
		if val != curr_freq:
			return False
	return True

assert iscool("ana") == False
assert iscool("col") == True
assert iscool("abc") == True
assert iscool(None) == True
assert iscool("") == True



