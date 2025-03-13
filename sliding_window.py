from collections import defaultdict

input = "aabbcc" 
#shortest contiguos substring  that contains at leats 3 uniqe characters
def find_shortest(input:str)->str:
    left, right = 0,0
    dict_freq = defaultdict(int)
    res = ''
    min_window_size = float('inf')

    for right in range(len(input)):
        dict_freq[input[right]] += 1
        while len(dict_freq.keys()) >= 3:
            if right - left + 1 <  min_window_size:
                min_window_size = right - left + 1
                res = input[left:right+1]
                dict_freq[input[left]] -= 1
                if dict_freq[input[left]] == 0:
                    del dict_freq[input[left]]
                left += 1
    return res

print(find_shortest(input)) #Output: 'abbcc'