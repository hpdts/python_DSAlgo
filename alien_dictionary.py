"""
Input: words[] = ["baa", "abcd", "abca", "cab", "cad"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "bdac".
The pair "baa" and "abcd" suggests 'b' appears before 'a' in the alien dictionary.
The pair "abcd" and "abca" suggests 'd' appears before 'a' in the alien dictionary.
The pair "abca" and "cab" suggests 'a' appears before 'c' in the alien dictionary.
The pair "cab" and "cad" suggests 'b' appears before 'd' in the alien dictionary.
So, 'b' → 'd' → 'a' → 'c' is a valid ordering.

baa
^
abcd
  ^
abca
   ^
cab

cad


b->d->a->c

d->a

a->c

b->d

Input: words[] = ["caa", "aaa", "aab"]
Output: true
Explanation: A possible corrct order of letters in the alien dictionary is "cab".
The pair "caa" and "aaa" suggests 'c' appears before 'a'.
The pair "aaa" and "aab" suggests 'a' appear before 'b' in the alien dictionary. 
So, 'c' → 'a' → 'b' is a valid ordering.

caa

aaa

aab

c->a->b

Input: words[] = ["ab", "cd", "ef", "ad"]
Output: ""
Explanation: No valid ordering of letters is possible.
The pair "ab" and "ef" suggests "a" appears before "e".
The pair "ef" and "ad" suggests "e" appears before "a", 
which contradicts the ordering rules.

ab
cd
ef
ad
a->c->e->a

"""
from collections import defaultdict

def is_alien_dictionary_ordered(words):
	# create graph
	graph = defaultdict(list)

	for word in words:
		for c in word:
			graph[c] = []

	for i in range(len(words) - 1):
		word1 = words[i]
		word2 = words[i+1]
		#print(f"word1: {word1}, word2: {word2}")
		word1_len = len(word1)
		word2_len = len(word2)
		if word1_len > word2_len and word1[:min_len] == word2[:min_len]:
			return ""
		min_len = min(word1_len, word2_len)

		for index_c in range(min_len):
			if word1[index_c] != word2[index_c]:
				graph[word1[index_c]].append(word2[index_c])
				break

	"""
	0 → unvisited
	1 → visiting (in recursion stack)
	2 → visited (done)
	"""
	visited = {}
	ret = []
	def dfs(node):
		if node in visited:
			return visited[node] == 2

		visited[node] = 1

		for neighbor in graph[node]:
			if not dfs(neighbor):
				return False

		visited[node] = 2
		ret.append(node)
		return True

	for node in graph:
		if node not in visited:
			if not dfs(node):
				return False



	#print(f"Graph: {graph}")
	return "".join(reversed(ret))

assert is_alien_dictionary_ordered(["ab", "cd", "ef", "ad"]) == False
assert is_alien_dictionary_ordered(["caa", "aaa", "aab"]) == "cab"
#print(is_alien_dictionary_ordered(["baa", "abcd", "abca", "cab", "cad"]))
assert is_alien_dictionary_ordered(["baa", "abcd", "abca", "cab", "cad"]) == "bdac"
print("All test cases passed!")


