def remove_subarray_sorted(arr):
    arr_sorted = sorted(arr)
    ret = []
    for start in range(len(arr)):
        if arr[start] != arr_sorted[start]:
            ret.append(start)
            break
    
    for end in range(len(arr)-1,-1,-1):
        #print(f"backwards arr[end]: {arr[end]}")
        if arr[end] != arr_sorted[end]:
            ret.append(end)
            break
    #print(f"ret: {ret}")
                 
    return ret

def printUnsorted(arr):
    n = len(arr)
    
    # create the temp array equal to arr
    temp = arr[:]
    
    # sort the temp array
    temp.sort()
    
    # to store the first and last index
    # with unmatching elements 
    s = 0
    e = 0
    
    # find the leftmost unmatching index
    for i in range(n):
        if arr[i] != temp[i]:
            s = i
            break
    
    # find the rightmost unmatching index
    for i in range(n - 1, -1, -1):
        if arr[i] != temp[i]:
            e = i
            break
    
    return [s, e]

"""
Fluctuation point
Find when desc and store min/max
Find start based on point
Find end based on point
[1,2,5,4,6] always arr[start] < arr[start+1]
     s 1

[1,2,5,4,6] always arr[end] > arr[err-1]
    -1 e
"""
def index_to_array_sorted(arr):
    ret = []
    for start in range(len(arr)):
        if start+1 < len(arr):
            if arr[start] > arr[start+1]:
                break
        start+=1

    if start == len(arr):
        return ret

    for end in range(len(arr)-1, -1, -1):
        if end-1 > 0:
            if arr[end] < arr[end-1]:
                break
        end-=1

    #print(f"start: {start}, end: {end}")

    min_num = arr[start] 
    max_num = arr[start]

    for i in range(start+1, end+1):
        min_num = min(arr[i], min_num)
        max_num = max(arr[i], max_num)


    for i in range(start):
        if arr[i] > min_num:
            start = i
            break

    for i in range(len(arr)-1, end, -1):
        if arr[i] < max_num:
            end = i
            break
    ret.append(start)
    ret.append(end)     
    return ret

assert remove_subarray_sorted([0, 1, 15, 25, 6, 7, 30, 40, 50]) == [2,5]
assert printUnsorted([0, 1, 15, 25, 6, 7, 30, 40, 50]) == [2,5]
assert remove_subarray_sorted([1,2,5,4,6]) == [2,3]
assert printUnsorted([1,2,5,4,6]) == [2,3]
assert remove_subarray_sorted([1,2,3,5,6,4,7,8,10,9]) == [3,9]
assert remove_subarray_sorted([2,1]) == [0,1]
assert remove_subarray_sorted([1,2,3,4,5]) == []
assert printUnsorted([1,2,3,5,6,4,7,8,10,9]) == [3,9]

assert index_to_array_sorted([0, 1, 15, 25, 6, 7, 30, 40, 50]) == [2,5]
assert index_to_array_sorted([1,2,5,4,6]) == [2,3]
assert index_to_array_sorted([1,2,3,5,6,4,7,8,10,9]) == [3,9]
assert index_to_array_sorted([2,1]) == [0,1]
assert index_to_array_sorted([1,2,3,4,5]) == []
print("all test cases pass")