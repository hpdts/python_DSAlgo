
from typing import List

def letterCasePermutation(s: str) -> List[str]:
    ret = []
    def helper(build, level):
        if level == len(s):
            ret.append(build)
            return

        for i in range(level, len(s)):
            char = s[i]
            if char.isalpha():
                helper(build+char.lower(), level+1)
                helper(build+char.upper(), level+1)
            else:
                helper(build+char, level+1) 
        
    helper("", 0)
    return ret


print(letterCasePermutation("a1b2"))