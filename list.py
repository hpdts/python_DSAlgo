"""
Hello

Swap kth node from end of singly linked list with head
                           k    
Input: 1->2->3->5
          H                   t
     
4->
h               c                    5
Temp = c.next         (4)
C.next = temp.next

Headtemp = head (1)
Head = temp4
Head.next = Headtemp

totalnodes = 5 -2 = 3 



Find k
Swap

1->2->3->4->5

K = 2
4->2->3->1->5

Temp = c.next  4

1->2->3->4->5
           c 

123


Temp = c.next.val (4)
C.next.val = head.val 




Swap the node




Encode: [USA, USA, USA, Mexico, Canada, Mexico, Mexico]
Result: [USA, Mexico, Canada, 0,0,0,1,2,1,1]

Decode:  [USA, Mexico, Canada, 0,0,0,1,2,1,1]
Result: [USA, USA, USA, Mexico, Canada, Mexico, Mexico]

Stock market:
Here’s a list of stock ticker symbols and their values
Give the optimal days to buy/sell

Trapping water


       1
1-2-3
H    t

K = 1


3-2-1



1->2->3->4->5
"""
class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.next = two
two.next = three
three.next = four
four.next = five

head = one


def print_list(head):
	curr = head
	result = []
	while curr:
		#print(f"{curr.val}->")
		result.append(f"{curr.val}")
		curr = curr.next
	return "->".join(result)

def kth_from_end(k):
	initialK = k
	curr = head
	pointer_k = head
	while k:
		if not pointer_k:
			raise ValueError(f"k={initialK} is larger than list")
		pointer_k = pointer_k.next
		k-=1
	#print(f"pointer_k.val: {pointer_k.val}")
	while pointer_k:
		curr = curr.next
		pointer_k = pointer_k.next

	#print(f"curr.val: {curr.val}")

	return curr


"""
try:
    kth_from_end(20)
except ValueError as e:
    assert str(e) == "k=20 is larger than the list"  # Ensure the correct exception is raised
else:
    raise AssertionError("Expected ValueError for k=20, but no exception was raised")
"""


"""
output: 

4->2->3->1->5
  thn p k
1->2->3->4->5
h  
2->3-*5
   2->3->1->5
4-> 
h   

4->2->3->1->5
"""
def get_k_1(head, kth):
	curr = head
	while curr:
		if curr.next == kth:
			return curr
		curr = curr.next
	return None

def swap_kth_node_from_end_with_head(head, k):
	#print(print_list(head))
	kth = kth_from_end(k)
	prev_kth = get_k_1(head, kth)
	temp_head_next = head.next
	head.next = kth.next
	prev_kth.next = head

	kth.next = temp_head_next
	head = kth
	#print(print_list(head))
	return head

assert print_list(head) == "1->2->3->4->5"
assert kth_from_end(2).val == 4
assert kth_from_end(1).val == 5
assert get_k_1(head, kth_from_end(2)).val == 3
newhead=swap_kth_node_from_end_with_head(head, 2)
							
assert print_list(newhead) == "4->2->3->1->5"

print("All assertions passed.")





