"""

Imagine that you operate a search engine for meeting transcripts. In the logs you notice that two queries, “launch smart summary” and “launching smart summaries”, produce different search results even though we can agree they are more or less equivalent. How can we detect that these two queries have the same meaning?

Here is sample input to get you started:

SYNONYMS = [
  ("launch", "launching"),
  ("summary", "summaries"),
]

QUERIES = [
  ("launch smart summary", "launching smart summary"),
  ("launch smart summary", "launch smart summaries"),
  ("smart summary launch", "launch smart summaries")
]
Your task is to output a list of boolean values such that each entry in the output indicates whether the corresponding pair of queries are equivalent.

("launch", "launching"),
("launching", "launch"),


True
True
False
dict

("launch smart summary", "launching smart summary")
split(' ')
len!= len


len == len
 if word == word2

 elif dict[word] == word2 or dict[word2] == word 
if 


"""


"""
SYNONYMS = [
  ("launch", "launching"),
  ("summary", "summaries"),
  ("launch", "ship"),
]

QUERIES = [
  ("launch smart summary", "launching smart summary"),
  ("launch smart summary", "launch smart summaries"),
  ("smart summary launch", "launch smart summaries")
]
"""

def create_dict(synonyms):
    synonyms_dict = {}
    for synonym in synonyms:
        synonym1, synonym2 = synonym[0], synonym[1]
        synonyms_dict[synonym1] = synonym2
        synonyms_dict[synonym2] = synonym1

    return synonyms_dict 


def run(synonyms, queries):
    ret = []
    # We will call your classes/functions here to execute unit tests
    synonyms_dict = create_dict(synonyms)
    print(synonyms_dict)
    """
    synonyms_dict = {}
    synonyms_dict["launch"] = "launching"
    synonyms_dict["launching"] = "launch"
    synonyms_dict["summary"] = "summaries"
    synonyms_dict["summaries"] = "summary"
    """
    for query in queries:
        #print(f"query: {query}")
        query1, query2 = query[0], query[1]
        split_q1, spli_q2 = query1.split(' '), query2.split(' ')
        # print(f"query1: {query1}, query2: {query2}")
        if len(split_q1) != len(spli_q2):
            ret.append(False)
        else:
            value_exp = True
            for index in range(len(split_q1)):
                word1 = split_q1[index]
                word2 = spli_q2[index]
                            
                if word1 == word2 or (word1 in synonyms_dict and synonyms_dict[word1] == word2) or (word2 in synonyms_dict and synonyms_dict[word2] == word1):
                    value_exp = True
                else:
                    value_exp = False
                    break
     
            ret.append(value_exp)
    #print(ret)
    #pass
    return ret

SYNONYMS = [
  ("launch", "launching"),
  ("summary", "summaries"),
]

QUERIES = [
  ("launch smart summary", "launching smart summary"),
  ("launch smart summary", "launch smart summaries"),
  ("smart summary launch", "launch smart summaries")
]

assert run(SYNONYMS, QUERIES) == [True, True, False]

QUERIES = [
  ("launch smart summary", "launching smart summary"),
  ("launch smart summary", "launch asdf summaries"),
  ("smart summary launch", "launch smart summaries")
]

assert run(SYNONYMS, QUERIES) == [True, False, False]

QUERIES = [
  ("launch smart summary test", "launching smart summary"),
  ("launch smart summary", "launching smart summary"),
  ("launch smart summary", "launch asdf summaries"),
  ("smart summary launch", "launch smart summaries")
]

assert run(SYNONYMS, QUERIES) == [False, True, False, False]
print("all test are passing")