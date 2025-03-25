"""
013
blastradius.ai/*
               ^
blastradius.ai/a
01234
bla/*
    ^
bla/a

[-1:index]

0
*blast*radius*
             ^

if not *

blast radius .ai


blastradius.ai/*tenantID=testID
                               ^
blastradius.ai/?id=fakeID&tenantID=testID contains tenantID=testID
blastradius.ai/*
               ^
*blast*radius* 
      s
      e


blastradius.a
     ^ 


substring(s+1, e)

prefix = blast
if s = *


start = 0
prefix = ''*
blastradius.ai 

***
"*****maria***d*","maria"
          

pattern      url
de ,         de
^           ^

p   u
  a ,  a, True
^   ^ 
0    0

ab, a, False
 ^  ^

ba, a, False
^  ^
*********ba


*ba, a, False
 ^  ^

*a, a, True
^ ^
                           pattern = * , match=frrr

                                empty
                              /        \
                            empty       r

                       

"""

def wildcard_match(pattern: str, url: str) -> bool:

    def helper(pattern_pointer, url_pointer):
      #print(f"pattern_pointer: {pattern_pointer}, url_pointer: {url_pointer}")
      if pattern_pointer == 0:
        return url_pointer == 0
      
      if url_pointer == 0:
        #the whole pattern should be stars
        # print(pattern_pointer)
        for i in range(pattern_pointer-1,-1,-1):
        #  print(pattern[i])
          if pattern[i] != '*':
            return False
        return True

      if pattern[pattern_pointer - 1] == url[url_pointer - 1]: #?? add here
        return helper(pattern_pointer - 1, url_pointer - 1)

      if pattern[pattern_pointer - 1] == '*':
        return helper(pattern_pointer, url_pointer - 1) or helper(pattern_pointer -1, url_pointer)

      return False


    # Split the pattern and URL into parts for subdomain validation
    def split_url(url):
        if '/' in url:
            domain, path = url.split('/', 1)
        else:
            domain, path = url, ''
        subdomains = domain.split('.')
        return subdomains, path

    # Validate subdomains and paths separately
    def validate_subdomains(pattern_subdomains, url_subdomains):
        while pattern_subdomains and url_subdomains:
            pattern_part = pattern_subdomains.pop()
            url_part = url_subdomains.pop()

            if pattern_part == '*':
                continue
            if pattern_part != url_part:
                return False

        # If there are remaining pattern parts, they must all be '*'
        while pattern_subdomains:
            if pattern_subdomains.pop() != '*':
                return False

        # If there are remaining URL parts, the pattern does not match
        return not url_subdomains

    # Split the pattern and URL into subdomains and paths
    pattern_subdomains, pattern_path = split_url(pattern)
    #print(f"pattern_subdomains: {pattern_subdomains}, pattern_path: {pattern_path}")

    url_subdomains, url_path = split_url(url)

    # Validate subdomains
    #if not validate_subdomains(pattern_subdomains, url_subdomains):
    #    return False

    #return helper(len(pattern_path), len(url_path))
    pattern_pointer = len(pattern)
    url_pointer = len(url)

    return helper(pattern_pointer, url_pointer)

    """
    #no reg ex
    if pattern == url:
      return True
    #elif pattern != url:
    # return False
    #start logic  
    prefix = ''
    start = 0
    end = start+1
    while start < len(pattern) and end < len(pattern):
      
      while end < len(pattern) and pattern[end] != '*':
        end+=1
      print(f"start: {start}, end: {end}")

      prefix = pattern[start+1:end]
      prefix_url = pattern[start+1:end]

      print(f"prefix: {prefix}, prefix_url: {prefix_url}")
      if prefix != prefix_url:
        return False
      else:
        start = end

      #start+=1
      end+=1

    print(f"start: {start}, end: {end}")
    print(f"pattern: {pattern[start]}, pattern[end]: {pattern[end]}")
    return False
    """



"""
      print(f"prefix: {prefix} , start: {start}")
     

      if start == 0:
        prefix = pattern[:start+1]
      else:
        prefix = pattern[start+1:start-1]
      print(f"prefix: {prefix} , start: {start}, url: {url}")

      if prefix != '*' and prefix not in url:
        print("herer")
        return False 
      start+=1
"""
paths = [
    ["","" , True],
    ["*","" , True],
    ["*****","" , True],
    ["*ba","a" , False],
    ["*****maria*","" , False],
    ["blastradius.ai", "blastradius.ai", True],  # exact match 
    ["waffles.com", "blastradius.ai", False],  # completely different
    ["*****maria*","maria" , True],
    ["blastradius.ai/a", "blastradius.ai", False],
    ["blastradius.a", "blastradius.ai", False],
    ["blastradius.ai/*", "blastradius.ai/a", True],  # basic route match
    ["*blast*radius*", "blastradius.ai", True],  # domain match
    ["blastradius.ai/?id=*", "blastradius.ai/?id=fakeID", True],  # query string match
    ["blastradius.ai/*tenantID=testID", "blastradius.ai/?id=fakeID&tenantID=testID", True],  # route match with query
    ["*.google.com/blah/*", "some-subdomain.blah.google.com/blah/something", True],  # subdomain match
    ["*.google.com/blah/*", "some-subdomain.blah.google.co.google.com/blah/something", True],  # subdomain match
    ["*blah.com*/hello", "blah.com/hello", True],  # ignoring wildcards for exact match
    ["*blah.com*/hello", "blah.com/ahello", False],  # no match
    ["*blah.com*/hello", "blaha.com/hhello", False],  # no match
    ["blah*blah", "blahasidjblahasidjblah", True], # match, but testing if the code ends too early
    # Wildcards:
    # additional tests for part 2. Ignore for now
    ## attempt to circumvent sudomain match with a different domain
    #["*.google.com/blah/*", "malicious-domain/blah.google.com/blah/something", False],

]
"""



    ## attempt to circumvent domain wildcard with sumdomain match with a different domain
    # ["*.google*.com/route", "otherdomain.com/b.google.com/route", False],
    ## more complex domain/subdomain match
    # ["*.google*.com/route", "b.google.otherdomain/something.com/route", False],
    ## match exact route
    # ["b*.c/h", "b.c/.c/h", False]
"""
for pattern, url, expected_result in paths:
    assert wildcard_match(pattern, url) == expected_result, f"Test failed for pattern: {pattern}, url: {url}"
    #print(f"{pattern} {url} {wildcard_match(pattern, url)} => expected {expected_result}")