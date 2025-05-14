#
# AI: Certainly!
# You can create a function that takes in a number and returns its reverse.
# Here’s how you can do it:
#

def reverse_number(num):
  negative = False
  if not num:
    return None
  if num < 0:
    negative = True
    num = abs(num)
  num_string = str(num)
  reverse_number = num_string[::-1]
  reverse = int(reverse_number)
  # Reverse the number
  #reverse = num[::-1]
  # Return the number
  return reverse if not negative else -reverse

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789

assert reverse_number(None) == None
assert reverse_number(-12) == -21
assert reverse_number(1223) == 3221
assert reverse_number(987654321) == 123456789
print("All tests passed!")


"""
def oppositeNumber(num):
    return -num

# Example usage:
print(oppositeNumber(5)) # Output: -5
print(oppositeNumber(-7)) # Output: 7
print(oppositeNumber(0)) # Output: 7
"""