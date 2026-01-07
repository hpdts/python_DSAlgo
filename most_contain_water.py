def maxWater_square(arr):
    n = len(arr)
    ret = 0

    for i in range(n):
        for j in range(i+1, n):
            curr_area = min(arr[i], arr[j]) * (j-i)
            ret = max(ret, curr_area)

    return ret

def maxWater(arr):
    l = 0
    r = len(arr) - 1
    ret = 0

    while l < r:
        curr_area = min(arr[l], arr[r]) * (r-l)
        ret = max(ret, curr_area)
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return ret
    
arr = [2, 1, 8, 6, 4, 6, 5, 5]
print(maxWater(arr))

