class LetterFilter:

    def __init__(self, s):
        self.s = s
        
# Enter your code here. 
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
# class LetterFilter:
#
#   def __init__(self, s):
#       self.s = s
    
    """
    ada
    d

    aeiotyi
    ^
    ty

    onomatopoeia
        ^
    nmtp



    """    
    def is_consonant(self, letter):
        #return letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'
        return letter not in 'aeiou'
        
    def filter_vowels(self): 
        word = self.s
        #print(f"word: {word}")
        ret = []
        for letter in word:
            #print(f"letter: {letter}")
            if self.is_consonant(letter):
                #print(f"letter filtered: {letter}")
                ret.append(letter)
        #print(f"ret: {ret}")
        return "".join(ret)
            
        
    def filter_consonants(self):
        word = self.s
        ret = []
        for letter in word:
            #if letter == 'aeiou':
            if not self.is_consonant(letter):
                ret.append(letter)
        return "".join(ret)
    

s = "onomatopoeia"
f = LetterFilter(s)
#print(f.filter_vowels())
#print(f.filter_consonants())
assert f.filter_vowels() == "nmtp"
assert f.filter_consonants() == "ooaooeia"
print("All test cases pass")