"""
Given an array of positive integers nums 
and a positive integer target, 
return the minimal length of a subarray whose 
sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
 
Example 1:
 
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] 
has the minimal length under the problem constraint.
Constraints:
1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

sliding window
[2,3,1,2,4,3]
         s
           e
 
s = 0
e = s+1

if nums[s] >= target
  return 1

ans = 0
sum(s..e)  >= target
 ans = length(s..e) 
 //change the window

e++


while e < len(nums) and s < e:

	curr_sum = nums[s] + nums[e]
	if 

sliding window

target = 7


 1 2 3 4 5 6
[2,3,1,2,4,3]
         s
           e
"""


def min_length(nums, target) -> int :
	start = 0
	curr_sum = 0
	min_len = float('inf')

	while start < len(nums):
		curr_sum = nums[start]
		if curr_sum >= target:
			return 1
		end = start + 1

		while end < len(nums):
			curr_sum+=nums[end]
			if curr_sum >= target:
				lenght_size = end - start + 1
				min_len = min(min_len, lenght_size)
				break
			end+=1

		start+=1
	return min_len

print(min_length([2,3,1,2,4,3], 7))
# O(n^2) time
assert min_length([2,3,1,2,4,3], 7) == 2

"""
 0 1 2 3 4 5
[2,3,1,2,4,3]
         L
             R
"""
def min_subarray_len(nums, target):
	left = 0
	min_len = float('inf')
	curr_sum = 0

	for right in range(len(nums)):
		curr_sum+= nums[right]

		while curr_sum >= target:
			min_len = min(min_len, right - left + 1)
			curr_sum-=nums[left]
			left+=1

	return 0 if min_len == float('inf') else min_len


