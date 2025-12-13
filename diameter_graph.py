#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. UNWEIGHTED_INTEGER_GRAPH networkA
#  2. UNWEIGHTED_INTEGER_GRAPH networkB
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
#


"""

//BFS
node at the last level d1 =2 

do BFS from that node till I find leave d2  d2-d1 =3 // 2

network A
dict(list)
1->2,3
2->1
3->1


network B
1->2
2->1,3
3->2


center

diameter 


diameter of A - > 2-1 + 1-4 = 2 / 2-1 + 1-3 = 2 //2 = 1
diameter of B -> 1-2 = 1//2 = 1


1+1+1= 3



diameter of final graph = 2a-1a + 1A-1B + 1b-2b = 3


"""
from collections import defaultdict, deque

def create_graph(networkA_nodes, networkA_from, networkA_to):
    graph = defaultdict(list)
    print(f"networkA_from: {networkA_from}")
    print(f"networkA_to: {networkA_to}")
    
    for index, node_from in enumerate((networkA_from)):
        graph[node_from].append(networkA_to[index])
        graph[networkA_to[index]].append(node_from)
        
    return graph

def node_longest_path(graph):
    #BFS
    q = deque([graph[0]])
    visited = set()
    
    while q:
        curr = q.popleft()
        
        #if not graph[curr]:
        #    return curr
        
        for nodes in graph[curr]:
            if nodes not in visited:
                q.push(nodes)
                visited.add(nodes)
    
    return None
    



def calculateMin(networkA_nodes, networkA_from, networkA_to, networkB_nodes, networkB_from, networkB_to):
    # Write your code here
    graph_a = create_graph(networkA_nodes, networkA_from, networkA_to)
    graph_b = create_graph(networkB_nodes, networkB_from, networkB_to)
    
    print(f"graph_a: {graph_a}")
    print(f"graph_b: {graph_b}")
    
    node_longest_path_graph_a = node_longest_path(graph_a)
    print(f"node_longest_path_graph_a: {node_longest_path_graph_a}")
    """
    diameter_a = find_path_from_node_to_leave(graph_a, node_longest_path_graph_a)
    radious_a = dist //2
    
    node_longest_path_graph_b = node_longest_path(graph_b)
    diameter_b = find_path_from_node_to_leave(graph_b, node_longest_path_graph_b)
    radious_b = dist //2
    
    return radious_a + radious_b + 1
    """
    return 0
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    networkA_nodes, networkA_edges = map(int, input().rstrip().split())

    networkA_from = [0] * networkA_edges
    networkA_to = [0] * networkA_edges

    for i in range(networkA_edges):
        networkA_from[i], networkA_to[i] = map(int, input().rstrip().split())

    networkB_nodes, networkB_edges = map(int, input().rstrip().split())

    networkB_from = [0] * networkB_edges
    networkB_to = [0] * networkB_edges

    for i in range(networkB_edges):
        networkB_from[i], networkB_to[i] = map(int, input().rstrip().split())

    result = calculateMin(networkA_nodes, networkA_from, networkA_to, networkB_nodes, networkB_from, networkB_to)

    fptr.write(str(result) + '\n')

    fptr.close()