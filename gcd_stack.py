import math

def are_relatively_prime(a: int, b: int) -> bool:
    print(f"gcd of {a} and {b} is {math.gcd(a,b)}")
    if math.gcd(a, b) > 1:
        return False
    else:
        return True

def solution(arr1: [int]) -> [int]:
    # write your solution here
    res = [ ]
    i = 0
    j = i +1
    while i < len(arr1) and j < len(arr1):
        if are_relatively_prime(arr1[i], arr1[j]): 
            res.append(arr1[i])
            res.append(arr1[j])
            i+=2 
            j=i+1
        else:
            lcm = math.lcm(arr1[i], arr1[j])
            if not res:
                res.append(lcm)
            elif res [-1] != lcm:
                res.append(lcm)
            arr1[j] = lcm
            i+=1
            j=i+1

    return res

def stack_sol(arr1):
    stack = []
    print(f"Initial arr1: {arr1}")
    for num in arr1:
        stack.append(num)
        print(f"stack after pushing {num}: {stack}")

        while len(stack) >= 2:
            a = stack[-1]
            b = stack[-2]
            print(f"top two elements: {a}, {b}")
            print(f"gcd of {a} and {b} is {math.gcd(a,b)}")
            if math.gcd(a, b) == 1:
                break

            lcm = math.lcm(a, b)
            print(f"lcm of {a} and {b} is {lcm}")
            stack.pop()
            stack.pop()
            stack.append(lcm)
            print(f"stack after replacing with lcm: {stack}")

    return stack


print(stack_sol([2,4,3,9]))
#print(stack_sol([4, 6, 9]))

#print(solution([4, 16]))
#print(solution([12, 36]))
#print(solution([4, 6, 9]))

assert stack_sol([4, 3]) == [4,3]
assert stack_sol([12, 36]) == [36]
#assert solution([4, 6, 8, 10]) == [120]
assert stack_sol([2, 1]) == [2, 1]
#assert solution([6, 10, 15]) == [30, 15]
#assert solution([3,4,12,7,6,2]) == [3,4,7,6,2]
assert stack_sol([4, 6, 9]) == [36]
assert stack_sol([2,4,3,9]) == [4,9]