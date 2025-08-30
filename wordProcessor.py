'''
We are building a word processor and we would like to implement a "word-wrap" functionality.

Given a list of words followed by a maximum number of characters in a line, return a collection of strings where each string element represents a line that contains as many words as possible, with the words in each line being concatenated with a single '-' (representing a space, but easier to see for testing). The length of each string must not exceed the maximum character length per line.

Your function should take in the maximum characters per line and return a data structure representing all lines in the indicated max length.

Examples:

words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) "wrap words1 to line length 13" =>

  [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]

wrapLines(words1, 12) "wrap words1 to line length 12" =>

  [ "The-day",
    "began-as",
    "still-as-the",
    "night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]    


wrapLines(words1, 20) "wrap words1 to line length 20" =>

  [ "The-day-began-as",
    "still-as-the-night",
    "abruptly-lighted",
    "with-brilliant-flame" ]

words2 = [ "Hello" ]

wrapLines(words2, 5) "wrap words2 to line length 5" =>

  [ "Hello" ]


wrapLines(words2, 30) "wrap words2 to line length 30" =>

  [ "Hello" ]  

words3 = [ "Hello", "Hello" ]

wrapLines(words3, 5) "wrap words3 to line length 5" =>

  [ "Hello",
  "Hello" ]

words4 = ["Well", "Hello", "world" ]

wrapLines(words4, 5) "wrap words4 to line length 5" =>

  [ "Well",
  "Hello",
  "world" ]

words5 = ["Hello", "HelloWorld", "Hello", "Hello"]

wrapLines(words5, 20) "wrap words 5 to line length 20 =>

  [ "Hello-HelloWorld",
    "Hello-Hello" ]


words6 = [ "a", "b", "c", "d" ]
wrapLines(words6, 20) "wrap words 6 to line length 20 =>

  [ "a-b-c-d" ]

wrapLines(words6, 4) "wrap words 6 to line length 4 =>

  [ "a-b",
    "c-d" ]

wrapLines(words6, 1) "wrap words 6 to line length 1 =>

  [ "a",
    "b",
    "c",
    "d" ]


wrapLines(words2, 3) "wrap words2 to line length 5" =>

  [ "Hello" ]
  
  
All Test Cases:
          words,  max line length
wrapLines(words1, 13)
wrapLines(words1, 12)
wrapLines(words1, 20)
wrapLines(words2, 5)
wrapLines(words2, 30)
wrapLines(words3, 5)
wrapLines(words4, 5)
wrapLines(words5, 20)
wrapLines(words6, 20)
wrapLines(words6, 4)
wrapLines(words6, 1)

n = number of words OR total characters
'''

words1 = ["The","day","began","as","still","as","the","night","abruptly","lighted","with","brilliant","flame"]
words2 = ["Hello"]
words3 = ["Hello", "Hello"]
words4 = ["Well", "Hello", "world"]
words5 = ["Hello", "HelloWorld", "Hello", "Hello"]
words6 = ["a", "b", "c", "d"]

# Note: built-in functions like the Python textwrap module should not be used as solutions to this problem.


"""
?? tricky Cases

The-day-began

while no more words
lineCharCounter = 13 / 9 / 5
lineWords = [];
if len(word) <= lineCharCounter 
 #out.add(word) 
 lineWords.add(word+'-')
 lineCharCounter-=len(word)+1
 else:
     break
 
 out.add(lineWords)
 
 
 length =3 
 The-day-beg
         ^+3 
 *+length        
    
    The
    day
    beg
                           *
     while len(s)+ 13 <   
                           
The-day-bega-as-still-as-the-night-abruptly
                                     ^              i+10
                          
                          

The-day-began


          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" 
             *
words1 = [ "The", "day", "began", "as", "still", "as", "the",
          "night", "abruptly", "lighted", "with", "brilliant",
          "flame" ]

wrapLines(words1, 13) "wrap words1 to line length 13" =>

curr_length = 4 8 13 
"The-
  [ "The-day-began",
    "as-still-as",
    "the-night",
    "abruptly",
    "lighted-with",
    "brilliant",
    "flame" ]
    
    
"""
def wrapLines(words, max_length):
  lines = []
  curr_length = 0
  ret = []

  for word in words:
    length_word = len(word)
    add_length = length_word if not lines else length_word + 1  
    if curr_length + add_length <= max_length:
      lines.append(word)
      curr_length+= add_length
    else:
      ret.append("-".join(lines))
      lines = [word]
      curr_length = length_word

  if lines:
    ret.append("-".join(lines))

  return ret

   

def wrapLines_bad(words, max_length):
    all_words = '-'.join([x for x in words])
    print(all_words)
    out = []
    i = 0
    while i < len(all_words):
        letter=all_words[i]
        print(letter)
        if letter == '-':
          i+=1
          break
          
        """
        sub_string_plus_one = all_words[i+1:max_length]
        print("sub_string_plus_one:", sub_string_plus_one)
        if sub_string_plus_one == '-':
            out.add(sub_string_plus_one) 
            i+=max_length
            break

            a-b-c
            ^
        """
                
        sub_string = all_words[i:max_length]
        print("sub_string:", sub_string)
        out.add(sub_string) 
        i+=max_length
        
        """
        find_hyphen = max_length    
        curr_word = sub_string
        while sub_string != '-':
            sub_string = curr_word[i:find_hyphen-1]
        
        out.add(sub_string) 
        i+=len(sub_string)
        """
    
    return out

#print(wrapLines(words1, 13))
assert wrapLines(words1, 13) == [ "The-day-began","as-still-as","the-night","abruptly","lighted-with","brilliant","flame" ]
assert wrapLines(words1, 12) == [ "The-day","began-as","still-as-the","night","abruptly","lighted-with","brilliant","flame" ]
assert wrapLines(words1, 20) == [ "The-day-began-as","still-as-the-night","abruptly-lighted","with-brilliant-flame" ]
assert wrapLines(words2, 5) == [ "Hello" ]
assert wrapLines(words2, 30) == [ "Hello" ]
assert wrapLines(words3, 5) == [ "Hello","Hello" ]
assert wrapLines(words4, 5) == [ "Well","Hello","world" ]
assert wrapLines(words5, 20) == [ "Hello-HelloWorld","Hello-Hello" ]
assert wrapLines(words6, 20) == [ "a-b-c-d" ]
assert wrapLines(words6, 1) == [ "a","b","c","d" ]


