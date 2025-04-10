#3 mistakes
def is_balanced_mine(input):
	stack=[]
	close_open = {}
	close_open[')'] = '('
	close_open['}'] = '{'
	close_open[']'] = '['
	close_open['>'] = '<'
	#print(f"close_open: {close_open}")
	for i in input:
		#c = input[i]
		c = i
		#print(f"i: {i}, c: {c}")
		if c in "({[>":
			stack.append(c)
		elif c in ")}]<":
			if not stack:
				return False
			par = stack.pop()
			if not close_open[c] == par:
				return False
		#print(f"stack: {stack}")
	if stack:
		return False
	else:
		return True
	

def is_balanced(input):
	stack=[]
	close_open = {')':'(','}':'{',']':'[','>':'<'}
	for i in input:
		if i in close_open.values():
			stack.append(i)
		elif i in close_open:
			if not stack or close_open[i] != stack.pop():
				return False
	return False if stack else True 


assert is_balanced("some string") == True
assert is_balanced("[abc(def)gh{i}j]") == True
assert is_balanced("[abcdef") == False
assert is_balanced("abcd(egf))") == False
assert is_balanced(")abcd((egf)") == False
assert is_balanced("(abcd[)]egfh") == False
print("All assertions passed")
