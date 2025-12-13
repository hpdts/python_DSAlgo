#
# AI: Certainly!
# You can create a function that takes in a number and returns its reverse.
# Here’s how you can do it:
#
def reverse_number_ori(num):
  # Reverse the number
  reverse = num[::-1]
  # Return the number
  return reverse
print(reverse_number_ori(1223)) # Output: 3221
#print(reverse_number_ori(987654321)) # Output: 123456789

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


def oppositeNumber(num):
    if not isinstance(num, (int, float)):
        return None
    if num == 0:
        return 0
    if not num:
      return None
    return -num

# Example usage:
print(oppositeNumber(5)) # Output: -5
print(oppositeNumber(-7)) # Output: 7
print(oppositeNumber(0)) # Output: 7

assert oppositeNumber(5) == -5
assert oppositeNumber(-7) == 7
assert oppositeNumber(0) == 0
assert oppositeNumber(None) == None
assert oppositeNumber("5") == None
print("All tests passed!")