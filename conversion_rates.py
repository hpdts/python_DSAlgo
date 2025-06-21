"""
Given a list of conversion rates as a collection of origin unit, destination unit, and  multiplier.

Design an algorithm that takes two arbitrary unit values and returns the conversion rate between them.



Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). 
Given some queries, return the answers. If the answer does not exist, return -1.0.



equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 


The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

foot inch 12

foot yard 0.3333333

etc…

a/b = 2.0

a = 

adj list


  2   3
a -> b -> c                --->
  <-   <- 
  1/2  1/3


DFS
BFS



c,a

b/c = 3

a
-  = 2
b


b 
-  = 
a

a = 2 b


1/2    = b/a



a/2 = b

1. a = 2 b
   
2. b = 3 c

3. a = 2( 3c) ->  from 1
4. a/c = 6 

c = b/3


 ["a", "c"],   
 
    6
a/b = 2.0 
b/a = 1/2.0

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

  2   3
a -> b -> c                --->
  <-   <- 
  1/2  1/3

TRIE

"""

from collections import defaultdict, deque

def solve_equations(equations, values, queries):
    def create_graph(equations, values):
        graph = defaultdict(list)
        for i in range(len(equations)):
            eq = equations[i]
            value = values[i]
            term1 = eq[0]
            term2 = eq[1]
            graph[term1].append((term2, value))
            graph[term2].append((term1, 1/value))       
        return graph
    
    def bfs(graph, from_node, to_node):
        if from_node not in graph or to_node not in graph:
            return -1.0
        queue = deque()
        queue.append((from_node, 1))
        visited = set()
        
        while queue:
            curr = queue.popleft()
            curr_node = curr[0]
            curr_value = curr[1]
            
            if curr_node == to_node:
                return curr_value
            
            visited.add(curr_node)
            for next_node,next_value in graph[curr_node]:
                if next_node not in visited:
                    queue.append((next_node, next_value * curr_value))

        return -1.0

    graph = create_graph(equations, values)
    #print(f"graph: {graph}")
    #BFS
    ret = []
    for query in queries:
        from_node = query[0]
        to_node = query[1]
        result = bfs(graph, from_node, to_node)
        #print(f"result: {result} for query: {query}")
        ret.append(result)
    
    return ret

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
 
#print(solve_equations(equations, values, queries))
assert solve_equations(equations, values, queries) == [6.0, 0.5, -1.0, 1.0, -1.0]   
print("All test cases passed!")    
    
    
    
    
    



""""""