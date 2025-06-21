"""

An analyst in the logistics team of e-commerce was 
reviewing the efficiency metrics of the new automated 
stocking and retrieval machines. 
They went about their calculations in the following manner:

A sequence of n machines is tasked with stocking or retrieving items. 
Given the individual stocking/retrieving capacity values 
of each machine as an integer array, machineCapacity.
The Efficiency of this sequence is evaluated
using a comparison metric: 
the sum of
the absolute difference between consecutive machine 
capacities.
The task is to determine whether achieving 
the same sum of the absolute difference
is possible by removing some machines from the sequence to streamline 
the operations. If it is possible, 
return the minimum number of machines required in the sequence 
to attain the same sum of the absolute difference between 
consecutive machine capacities.
It's important to note that the number
of machines in the sequence must always be
greater than O. If achieving the same sum is impossible on removal, 
return n, which is the original number of machines in the sequence.

Note: The efficiency score of a consisting of only one machine is O.


Example
n = 5

machineCapacity = [1, 2, 2, 1, 1]

1 2 2 1 1 -> 1 2 1


Efficiency initially: |1 - 2| + |2 - 21 +12-11 + 11 11 = 2
Efficiency after removal: 11-21 + 12 - 11 = 2
1
2
1
It can be seen that after the removal of these 2 machines, we obtain the sc03-65
efficiency.
Thus, the answer in this case is 3.
amazon_hook
It can be proven that the answer can't be less than 3.
om
Function Description
63 complete the function findMinimum MachinesSize in the editor below.
findMinimumMachinesSize has the following parameter(s):
onfidential
int machineCapacity[n]: the stocking/retrieval capacity of each machine
Returns
pazon_hook+66
int: the minimum number of machines in the sequence required 
to achieve the same performance score

machineCapacity = [5, 4, 0, 3, 3, 1]
output = 4

5 4 0 3 3 1 -> 5 0 3 1



"""
"""

total_performance = get_efficiency(machineCapacity)
print(f"total_performance: {total_performance}")
machineCapacitytemp = machineCapacity
n = len(machineCapacity)
ret = []
for i in range(n):
	del machineCapacitytemp[i]
	print(f"temp array: {machineCapacitytemp}")
	curr_performance = get_efficiency(machineCapacity)
	print(f"curr_performance: {curr_performance}, index: {i}")
	if curr_performance != total_performance:
		ret.append(i)
	machineCapacitytemp = machineCapacity

print(f"ret: {ret}")

return ret
	def get_efficiency(machineCapacity):
		total_performance = 0
		for i in range(len(machineCapacity)-1):
			curr_performace = abs(machineCapacity[i] - machineCapacity[i+1])
			total_performance+=curr_performace
		return total_performance

	total_performance = get_efficiency(machineCapacity)
"""
def findMinimumMachinesSize(machineCapacity):
	n = len(machineCapacity)
	result = [machineCapacity[0]]
	for i in range(1,n):
		result.append(machineCapacity[i])

		while len(result) >= 3:
			first, mid, end = result[-3], result[-2], result[-1]
			if abs(first - mid) + abs(mid - end) == abs(first - end):
				result.pop(-2)
			else: 
				break
	print(f"result: {result}")
	return len(result)


#print(findMinimumMachinesSize([1,2,2,1,1]))
assert findMinimumMachinesSize([5, 4, 0, 3, 3, 1]) == 4
assert findMinimumMachinesSize([1,2,2,1,1]) == 3



"""
provides scalable cloud computing services. 
user has designed architecture that uses vertical scaling 
where computers are serially connected with one another.

The strength of the machines is represented by an array machines, 
where the ith element of the array represents the strength of the ith 
machine. The cost connecting a machine at index i to a machine at 
index i + 1 is defined as |machines [i+1]-machines[i]|. 
In order to reduce some costs, the user has decided to remove 
some machines from the system. 
To avoid a lot of reconnections, the user decides to remove 
any k consecutive machines from the system such that the total cost 
of the remaining system is minimized.
Given a positive integer array machines, and an integer k, 
remove exactly
k consecutive machines from the system such 
that the total sum of differences of the consecutive 
machine strengths is minimized.

Example
HackerRank
machines = [3, 9, 4, 2, 16]
k = 3
amazon_hook+6628fc03-653c-44d8-bc8
Currently, the cost is 
|9 - 3| + |4 - 9| + |2 - 4| + |16 - 2| = 6 + 5 + 2 + 14 = 27 
The following are all the consecutive set of machines that we can delete:

Delete [3, 9, 4]
fidential
39 4
2
16
-
2 16
8fc03-653c-44
Delete [9, 4, 2]
3
9 4
2
16
Delete [4, 2, 16]
3
9 4 2
16
Cost: 2-16 14
=
3 16
al
Cost: 3-16 13|
=
mazon_hook+6628fc03-
The minimum cost is 6.
Function Description
3
9
Cost: 3-96
nfidential
Complete the function minimizeSystemCost in the editor belomazon_hook+66
minimizeSystemCost has the following parameters:
sden
"""

machines = [3, 9, 4, 2, 16]
k = 3

def minimizeSystemCost(machines, k):
	n = len(machines)

	total_cost = sum(abs(machines[i+1] - machines[i]) for i in range(n - 1))
	print(f"total_cost: {total_cost}")
	min_cost = float('inf')

	for start in range(n - k + 1):
		print(f"start: {start}")
		#window_cost = sum(abs(machines[i+1] - machines[i]) for i in range(k,n-1))
		#print(f"window_cost: {window_cost}")
		removed_cost = 0
		for i in range(start, start + k -1):
			print(f"i: {i}")
			removed_cost+=abs(machines[i+1] - machines[i])
		print(f"removed_cost: {removed_cost}")
		
		if start > 0:
			removed_cost+=abs(machines[start]-machines[start-1])

		if start + k < n:
			removed_cost+=abs(machines[start+k]-machines[start+k-1])

		add_cost = 0
		if start > 0 and start + k < n:
			add_cost = abs(machines[start + k] - machines[start-1])

		new_cost = total_cost - removed_cost + add_cost
		print(f"add_cost: {add_cost}, new_cost: {new_cost}")

		min_cost = min(min_cost, new_cost)

	return min_cost

#print(f"minimizeSystemCost: {minimizeSystemCost(machines, k)}")

assert minimizeSystemCost([3, 9, 4, 2, 16], 3) == 6
#print(f"minimizeSystemCost([5,4,0,3,3,1], 2): {minimizeSystemCost([5,4,0,3,3,1], 2)}")
#assert minimizeSystemCost([5,4,0,3,3,1], 2) == 10
