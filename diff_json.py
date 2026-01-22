import json
"""
DFS
ret=""
by level and see the key
    if not diff: 
        add user_json
        
 user_json k,v
 
    diff_json k,v
    
    
    if user_json[k] is dict
      dfs(diff_json[k])
    else:
        search in all keys
        if its there replace it to ret
        otherwise      add it  

"""


user_json = """{
    "first_name": "John",
    "email": "abc@gmail.com",
    "favorite_colors": ["blue", "orange"],
    "favorite_team": {
      "name": "Washington Football Team",
      "favorite_player": "Chase Young",
      "city": "Washington DC"
    }
}"""

diff_json = """{
    "email": "example@braze.com",
    "favorite_colors": ["red", "green"],
    "favorite_team": {
      "favorite_player": "Terry McLaurin",
      "city": null
    },
    "last_name": "Smith"
}"""
 
user = json.loads(user_json)
diff = json.loads(diff_json)
"""
print("User")
for key, value in user.items():
    print(key, '->', value)
    
print("Diff")
for key, value in diff.items():
    print(key, '->', value)
""" 


def diff_dfs(user, diff, ret, key):
    #base case
    if not user and not diff:
        return ret
    if not user:
        ret[key] = diff
        return ret
    if not diff:
        ret[key] = user
        return ret
    
    for key, value in user.items():
        if isinstance(user[key], dict):
            #ret[key] = {}
            ret = diff_dfs(user[key], diff[key], ret, key)
        else:
            if key in diff:
                ret[key] = diff[key]
            else:
                #print(f"key: {key}, value: {value}")
                ret[key] = value
    """
    # missing key on diff
    for key, value in diff.items():
        if isinstance(diff[key], dict):
            ret = diff_dfs(diff[key], user[key], ret)
        else:
            if key in user:
                ret[key] = user[key]
            else:
                ret[key] = value
    """
            
    return ret
    
# print(diff_dfs(user, diff, {}, ""))
    
def diff_dfs_gpt(user, diff):
    result = {}

    # keys from both dicts
    all_keys = set(user.keys()) | set(diff.keys())

    for key in all_keys:
        user_val = user.get(key)
        diff_val = diff.get(key)

        if key in diff and diff_val is None:
            continue
            
        # both are dicts → recurse
        if isinstance(user_val, dict) and isinstance(diff_val, dict):
            result[key] = diff_dfs_gpt(user_val, diff_val)

        # key exists in diff → diff wins (even if None)
        elif key in diff:
            result[key] = diff_val

        # key only in user
        else:
            result[key] = user_val

    return result
    
print(diff_dfs_gpt(user, diff))  
    
    
    