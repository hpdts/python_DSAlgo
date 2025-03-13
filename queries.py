def answerQueries(queries: list, N: int) -> list:  
    def findNextTrueFromIndex(index) -> int:
        index = index
        for i in range(index, len(bools)):
            if bools[i]:
                return i + 1
        return -1  # No True found
    
    bools = [False for _ in range(N)]
    res = []
    for query in queries:
        type_query, index = query[0], query[1]
        index = index - 1
        
        if type_query == 1:
            bools[index] = True
        else:
            index_true = findNextTrueFromIndex(index)
            res.append(index_true)
    return res

queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]]
output = [-1, 2, -1, 2]
res = answerQueries(queries, 5)
print(res)
