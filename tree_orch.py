"""
Org Cost Rollup
Problem Statement
You are given a company’s organization represented as a tree.

Each employee:

has a unique integer ID 0 .. n-1

has at most one manager

may own cloud accounts that generate a direct monthly cost

The CEO has no manager (-1).

Input

n – number of employees

manager[i] – manager of employee i, or -1 if i has no manager

direct_cost[i] – direct cloud cost of employee i

queries – a list of employee IDs; for each employee x, return the total cost of the org subtree rooted at x.

The total org cost for an employee x is:

total_cost(x) = sum of direct_cost[i] for all employees i in x’s subtree (including x)

Example Walkthrough
n = 5
                0  1. 2. 3. 4
manager     = [-1, 0, 0, 1, 1]

                0  1. 2. 3. 4
direct_cost = [ 8, 3, 2, 5, 1 ]

queries     = [0, 1, 3]

org chart:
        0(cost(8))
      /   \
    1     2.       
  /   \
  3     4
  
employee.   subtree.      cost 

0    {0, 1, 2, 3, 4}    8 + 3 + 2 + 5 + 1 = 19

1    {1, 3, 4}    3 + 5 + 1 = 9
3    {3}    5

Output: [19, 9, 5]
Starter Code

tree n-ary
//BFS
dict<Node, cost>
class Node:
    


"""
from typing import List
from collections import defaultdict, deque



class Solution:
    class Node:
        def __init__(self, node_id, children=None):
            self.id = node_id,
            self.children = defaultdict(list)
    """
                    0  1. 2. 3. 4
    manager     = [-1, 0, 0, 1, 1]
         0(cost(8))
      /   \
    1     2.       
  /   \
  3     4

0=> 1,2
1=>3,4
    """
    def create_tree(self, manager):
        tree = defaultdict(list) 
        #print(f"manager: {manager}")
        for index in range(len(manager)):
         #   print(f"index: {index}")
            tree[index] = []
            
        for index in range(len(manager)):
            father = manager[index]
          #  print(f"index: {index}, father: {father}")
            if father != -1:
                tree[father].append(index)
        
        return tree
        
    def create_cost_dict(self, direct_cost):
        cost_dict = {}
        for index, cost in enumerate(direct_cost):
            cost_dict[index] = cost
        return cost_dict
    
    """
        0(cost(8))
      /   \
    1     2.       
  /   \
  3     4

    """
    def calculate_cost_BFS(self, start_node, graph, cost_dict):
        q = deque([(start_node, cost_dict[start_node])])
        ret = 0
        while(q):
            (curr, curr_cost) = q.popleft()
            
            ret+=curr_cost

            if curr in graph:
                for child in graph[curr]:
                    q.append((child, cost_dict[child]))

        return ret
        
        
        
    def org_cost_rollup(
        self,
        n: int,
        manager: List[int],
        direct_cost: List[int],
        queries: List[int]
    ) -> List[int]:
        """
        Return total org cost for each employee in `queries`.
        """
        tree = self.create_tree(manager)
        #print(f"tree: {tree}")
        cost_dict = self.create_cost_dict(direct_cost)
        #print(f"cost_dict: {cost_dict}")
        ret = []
        for q in queries:
            cost = self.calculate_cost_BFS(q, tree, cost_dict)
            ret.append(cost)
        #print(f"ret: {ret}")
        return ret

n = 5
manager     = [-1, 0, 0, 1, 1]
direct_cost = [ 8, 3, 2, 5, 1 ]
queries     = [0, 1, 3]

sol = Solution()
#print(sol.org_cost_rollup(n,manager, direct_cost, [0]))
assert sol.org_cost_rollup(n,manager, direct_cost, [0]) == [19]
assert sol.org_cost_rollup(n,manager, direct_cost, queries) == [19, 9, 5]
print("all asserts passed")