"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""
def fizzbuzz(n: int):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def fizzbuzzParameterizedversion(n: int, fizz=3, buzz=5):
    for num in range(1, n+1):
        if num % fizz == 0 and num % buzz == 0:
            print("FizzBuzz")
        elif num % fizz == 0:
            print("Fizz")
        elif num % buzz == 0:
            print("Buzz")
        else:
            print(num)

#fizzbuzzParameterizedversion(15, fizz=2, buzz=7)
def fizzbuzz_dict(n: int, rules=None):
    if not rules:
        rules = {3:"Fizz", 5:"Buzz"}
    
    for i in range(1, n+1):
        #output = "".join(word for num, word in rules.items() if i % num == 0)
        #print(output or i)
        output = ""
        for num_rule, word in rules.items():
            #print(f"num_rule: {num_rule}, word: {word}")
            if i % num_rule == 0:
                output = word
                break
        if output:
            print(output)
        else:
            print(i)

fizzbuzz_dict(10, {3:"Fizz", 5:"Buzz", 7:"Jazz"})

def fizzbuzz_func(n):
    print("\n".join(
        "Fizzbuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 == 0 else
        str(i)
        for i in range(1, n +1)
    ))
fizzbuzz_func(12)

def fizz_buzz_generator(n)
    def 
