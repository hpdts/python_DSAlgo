"""
We define super digit of an integer x using the following rules:
Given an integer, we need to find the super digit of the integer.
·         If x has only 1 digit, then its super digit is x.
·         Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
For example, the super digit of 9875 will be calculated as:
                    super_digit(9875)     9+8+7+5 = 29
                    super_digit(29)          2 + 9 = 11
                    super_digit(11)                              1 + 1 = 2
                    super_digit(2)                                = 2 
 
superDigit has the following parameter(s):
·         string n: a string representation of an integer
·         int k: the times to concatenate n to make p
Returns
·         int: the super digit of n repeated k  times

Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city doesn't connect with the last city. Determine the maximum distance from any city to its nearest space station
Example
There are n=3 cities and city 1 has a space station. They occur consecutively along a route. City 0 is 1-0 = 1 unit away and city 2 is 2-1 = 1 units away. City 1 is 0 units from its nearest space station as one is located there. The maximum distance is 1.
"""

# An n-gram, which is used in linguistics, refers to a contiguous sequence of N
# items from a given sequence of text.

# Example:
# Suppose we have the following sentences.
# "the cow jumped over the moon"
# "the cow and the moon"

# The unique 2-grams would be:
# "the cow"
# "cow jumped"
# "jumped over"
# "over the"
# "the moon"
# "cow and"
# "and the"


# Given a list of reviews, we want the frequency of all N-grams, where N is a
# parameter. If we use the following reviews:
# "the cow jumped over the moon"
# "the cow and the moon"


# "the cow cow cow jumped over the moon"
# "the cow cow cow and the moon"
#the cow = 1
# cow cow  = 4
# And we use N=2, then the expected result is:
# "the cow" ⇒ 2
# "cow jumped" ⇒ 1
# "jumped over" ⇒ 1
# "over the" ⇒ 1
# "the moon" ⇒ 2
# "cow and" ⇒ 1
# "and the" ⇒ 1
#spaces separation 
#N is the number of qty of anagrams
#many reviews, they need to be together, contiguous sequence

# "the cow jumped over the moon"
"""
lr1 = the cow, cow jumped, jumped over ...
dict=                            ^
lr2 = the cow, cow and,
         ^
lr3 = gt d, hy d, ana d         
# "the cow and the moon"      
         
ret set= the cow = 2

def get_ngrams(n)->list:
     
# "the cow and the moon"

def addNumbers(a,b):
    sum = a + b
    return sum

num1 = int(input())
num2 = int(input())

print("The sum is", addNumbers(num1, num2))
""" 
# "the cow jumped over the moon"
from collections import defaultdict
def get_groups_words_n(n, text):
    #ret = []
    words = text.split(" ")
    freq = defaultdict(int)
    #print(f"words: {words}")
    i = 0
    while i <= len(words) - n:
        groups = []
        #2 pointers approach
        for j in range(i, i+n):
            #print(f"word j n times: {words[j]}")
            groups.append(words[j])

        key = " ".join(groups)
       # ret.append(key)
        freq[key]=freq[key]+1
        i+=1
    #print(f"freq: {freq}")
    return freq

# try cow cow
#print(get_groups_words_n(2, "the cow jumped over the moon"))
# And we use N=2, then the expected result is:
# "the cow" ⇒ 2
# "cow jumped" ⇒ 1
# "jumped over" ⇒ 1
# "over the" ⇒ 1
# "the moon" ⇒ 2
# "cow and" ⇒ 1
# "and the" ⇒ 1
reviews = ["the cow jumped over the moon", "the cow and the moon"]

def n_gram(n, reviews):
    def get_value_other_reviews(phrase, dicts_reviews, index_dict):
        value = 0
        for i in range(len(dicts_reviews)):
            #print(f"phrase: {phrase}, index_dict: {index_dict}, i: {i}")
            if i != index_dict:
                dict_review = dicts_reviews[i]
                value+= dict_review.get(phrase, 0)
            #    print(f"value: {value}")
        
        return value


    dicts_reviews = []
    for review in reviews:
        dict_review = get_groups_words_n(n, review)
       # dicts_reviews.append(dict_review)
        dicts_reviews.append(dict_review.copy())

    #search in all maps
    ret = []
    #print(f"Before loop: {dicts_reviews}")
    seen = set()
    for index_dict in range(len(dicts_reviews)):
        dict_review = dicts_reviews[index_dict]
        for key, value in dict_review.items():
            if key not in seen:
               # print(f"BEFORE key: {key}, index_dict: {index_dict}")
                value_other_reviews = get_value_other_reviews(key, dicts_reviews, index_dict)
               # print(f"value: {value}, value_other_reviews: {value_other_reviews}")
                ret.append(f"{key} => {value + value_other_reviews}")
                seen.add(key)
   # print(f"After loop: {dicts_reviews}")
    return ret

assert n_gram(2, reviews) == ['the cow => 2', 'cow jumped => 1', 'jumped over => 1', 'over the => 1', 'the moon => 2', 'cow and => 1', 'and the => 1']
print("All assertions passed")

def get_freq_ngrams(n, review):
    freq = defaultdict(int)
    words = review.split(" ")
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i:i+n])
        freq[ngram] += 1
    return freq

def n_gram(n, reviews):
    # Aggregate n-gram counts across all reviews
    aggregated_counts = defaultdict(int)
    
    for review in reviews:
        review_ngrams = get_freq_ngrams(n, review)
        for ngram, count in review_ngrams.items():
            aggregated_counts[ngram] += count

    # Format the result
    ret = [f"{ngram} => {count}" for ngram, count in aggregated_counts.items()]
    return ret

assert n_gram(2, reviews) == ['the cow => 2', 'cow jumped => 1', 'jumped over => 1', 'over the => 1', 'the moon => 2', 'cow and => 1', 'and the => 1']
print("All assertions passed")

def get_freq_ngrams(n, review):
    freq = defaultdict(int)
    words = review.split(" ")
    i = 0
    while i < len(words):
        gram = []
        for k in range(i,i+n):
            #print(f"i: {i}, k:{k}")
            if k < len(words):
                gram.append(words[k])
        if len(gram) == n:
            key = " ".join(gram)
        
        freq[key]=freq[key]+ 1
        i+=1
    return freq
#print(get_freq_ngrams(2, "the cow jumped over the moon"))
#assert  get_freq_ngrams(2, "the cow jumped over the moon") == "{'the cow': 1, 'cow jumped': 1, 'jumped over': 1, 'over the': 1, 'the moon': 2}"  
""" 
rev1 = get_freq_ngrams(2, "the cow jumped over the moon")
rev2 = get_freq_ngrams(2, "the cow and the moon")

for key,val in rev1.items():
    
# "the cow" ⇒ 2
# "cow jumped" ⇒ 1
# "jumped over" ⇒ 1
# "over the" ⇒ 1
# "the moon" ⇒ 2
# "cow and" ⇒ 1
# "and the" ⇒ 1

"""


def n_gram(n, reviews):
    reviews_dict = []
    
    for review in reviews:
        rev_dict = get_freq_ngrams(n, review)
        reviews_dict.append(rev_dict)
    
    ret = []
    i=0
    seen_already=set()
    while i < len(reviews_dict):
        curr_dict = reviews_dict[i]
        for k in range(len(reviews_dict)):
            if k == i:
                continue
            next_dict = reviews_dict[k]   
            for key, value in curr_dict.items(): 
                   
                if next_dict[key]:
                    count = next_dict[key] + value
                    ret.append((key, count))
                seen_already.add(key)
        i+=1
    return ret
            
    

#print(n_gram(2, ["the cow jumped over the moon", "the cow and the moon"]))
     
    
    
    
     







