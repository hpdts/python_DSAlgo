'''
You are running a classroom and suspect that some of your students are passing around the answer to a multiple-choice question disguised as a random note.

Your task is to write a function that, given a list of words and a note, finds and returns the word in the list that is scrambled inside the note, if any exists. If none exist, it returns the result "-" as a string. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:  
words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
map_freq = b:2 a:1 y:1 ...

c:1 a:1 t:1
c:2
ccat
note_freq = c:1 t : 1 a :1 y: 1
   c is ther and freq word >= freqnote
   
   else return false           



caty substring 
note1 = "ctay"
find(words, note1) => "cat"   (the letters do not have to be in order)  
  
note2 = "bcanihjsrrrferet"
find(words, note2) => "cat"   (the letters do not have to be together)  
  
note3 = "tbaykkjlga"
find(words, note3) => "-"     (the letters cannot be reused)  
  
note4 = "bbbblkkjbaby"
find(words, note4) => "baby"    
  
note5 = "dad"
find(words, note5) => "-"    
  
note6 = "breadmaking"
find(words, note6) => "bird"    

note7 = "dadaa"
find(words, note7) => "dada"    

All Test Cases:
find(words, note1) -> "cat"
find(words, note2) -> "cat"
find(words, note3) -> "-"
find(words, note4) -> "baby"
find(words, note5) -> "-"
find(words, note6) -> "bird"
find(words, note7) -> "dada"
  
Complexity analysis variables:  
  
W = number of words in `words`  
S = maximal length of each word or of the note  
same freq or more??
words=cat

notes:
cat ret= cat

c ret="_"

cata ret = cat

'''


words = ["baby", "referee", "cat", "dada", "dog", "bird", "ax", "baz"]
note1 = "ctay"
note2 = "bcanihjsrrrferet"
note3 = "tbaykkjlga"
note4 = "bbbblkkjbaby"
note5 = "dad"
note6 = "breadmaking"
note7 = "dadaa"


#completeness
"""

c:2
ccat
note_freq = c:1 t : 1 a :1 y: 1
   c is ther and freq word >= freqnote
   
   else return false     
word:

c:1 a:1 t:1


note " ctay"
c: 0       

"""
from collections import Counter

def compare_dict_greater_equal(word_map, note_map):
   # print(f"word_map: {word_map}")    
   # print(f"note_map: {note_map}")

    for key_word in word_map.keys():
        key_word_freq = word_map[key_word]
       # print(f"key_word: {key_word}")        
       # print(f"key_word_freq: {key_word_freq}")

        if key_word not in note_map:
            return False
        elif key_word_freq > note_map[key_word]:
       #     print(f"note_map[key_word]: {note_map[key_word]}")
            return False
            
    return True 
    

def find(words, note):
    ret = '-'
    note_map = Counter(note)
    
    for word in words:
        word_map = Counter(word)
     #   print(compare_dict_greater_equal(word_map, note_map))
        if compare_dict_greater_equal(word_map, note_map):
            return word
        
        
    #print(note_map)
    return ret
"""
Runtime O(W*S)
Space O(W)

W + 1

"""
#assert find(words, note1) == "cat"
#print(find(words, note2))

assert find(words, note2) == "cat"
assert find(words, note3) == "-"
assert find(words, note4) == "baby"
assert find(words, note5) == "-"
assert find(words, note6) == "bird"
assert find(words, note7) == "dada"


print("All Assertions passed")
