def two_sum(nums, target):
	ret = []
	compl = {}
	for i, num in enumerate(nums):
		complement = target - num
		#print(f"complement: {complement}")
		if complement in compl:
			#print(f"here")
			ret.append(compl[complement])
			ret.append(i)
			return ret
		compl[num] = i
		#print(f"compl: {compl}")
	return ret


#print(two_sum([2,7,11,15], 9))
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([1,3,3,15], 6) == [1,2]
assert two_sum([1], 2) == []
print("all assertions passed")