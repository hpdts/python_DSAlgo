"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

"Hello","World"
  5        5

5#Hello5#World
i
 j


"""
def encode(strs: list[str]) -> str:
	ret = ""
	for word in strs:
		ret+= str(len(word)) + "#" + word
	return ret

def decode(s: str) -> list[str]:
	ret = []
	i = 0 
	while i < len(s):
		j = i
		while s[j] != '#':
			j+=1

		length = int(s[i:j])
		ret.append(s[j+1:j+1+length])
		i = j+1+length	

	return ret



dummy_input = ["Hello","World"]
encode_str = "5#Hello5#World"
assert encode(dummy_input) == encode_str
assert decode(encode_str) == dummy_input
print("all test cases passed")

