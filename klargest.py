"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

nums = [3,2,1,5,6,4], k = 2
                  ^

res = 5
max_heap=[6,5,3,4,2,1]
min_heap == k

6
7


"""
from collections.abc import Collection
import heapq

#from collections import heapq
def kth_largest(nums, k):
    max_heap = []

    #n log k
    for num in nums:
        heapq.heappush(max_heap, -num)

    ret = -1
    while k:
        ret = -heapq.heappop(max_heap)
        k-=1
    return ret


def kth_largest_min(nums, k):
    min_heap = []

    # Maintain a min-heap of size k
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:  # If the heap size exceeds k, remove the smallest element
            heapq.heappop(min_heap)

    # The root of the heap is the kth largest element
    return min_heap[0]

# time O(NlogN)
# space O(N)

# assume K<<N



nums = [3,2,1,5,6,4]
k = 2
#print(kth_largest(nums,k))
assert kth_largest(nums,2) == 5
assert kth_largest(nums,1) == 6
assert kth_largest_min(nums,2) == 5
assert kth_largest_min(nums,1) == 6
print("All assertions are passing")