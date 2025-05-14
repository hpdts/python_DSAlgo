#hello
"""
ana

s.isinstance
s < e

oso
s.e 
catc
 se

"""


def is_palindrome_old(input):
    s, e = 0, len(input)-1
    skip = 1
    while s < e:
        if input[s] != input[e]:
            #print(f"skip: {skip}, s: {input[s]}, e:{input[e]}")
           # is_palindrome(s+1,e) or is_palindrome(s,e-1)
            if skip == 1:
                skip-=1
                e-=1
                continue
            else:
                return False
        s+=1
        e-=1
        
    return True
    
def is_palindrome(input):
    s, e = 0, len(input)-1
    skip = 1
    while s < e:
        if input[s] != input[e]:
            #print(f"skip: {skip}, s: {input[s]}, e:{input[e]}")
           # is_palindrome(s+1,e) or is_palindrome(s,e-1)
            if skip == 1:
                skip-=1
                e-=1
                continue
            else:
                return False
        s+=1
        e-=1
        
    return True
    
def check_palindrome(input, s, e):
    while s < e:
        if input[s] != input[e]:
                return False, s, e 
        s+=1
        e-=1
    return True, s, e  

def helper(input, s, e, level):
    if s > e:
        return False
    if level > 1:
        return False
    res, s_check, e_check =  check_palindrome(input, s, e) 
    #print(f"res: {res}, s_check: {s_check}, e_check: {e_check}")
    if res:
        return True
    else:
        return helper(input, s_check+1, e_check, level+1) or helper(input, s_check, e_check-1, level+1)
        

def is_palindrome_interview(input):
    if not input:
        return True
    return helper(input, 0, len(input)-1, 0)
    
def is_palindrome(input):
    def check_palindrome(s, e):
        while s < e:
            if input[s] != input[e]:
                return False, s, e
            s += 1
            e -= 1
        return True, s, e

    def helper(s, e, skips):
        if skips > 1:  # Allow at most one character removal
            return False
        res, s_check, e_check = check_palindrome(s, e)
        if res:
            return True
        # Try skipping one character from either side
        return helper(s_check + 1, e_check, skips + 1) or helper(s_check, e_check - 1, skips + 1)

    if not input:
        return True
    return helper(0, len(input) - 1, 0)

#print(is_palindrome("madcam"))

assert is_palindrome("amadam") == True
assert is_palindrome("madam") == True
assert is_palindrome("cat") == False
assert is_palindrome("") == True
assert is_palindrome("madcam") == True
assert is_palindrome("catc") == True
assert is_palindrome("catcg") == False
print("all assertions passed")
