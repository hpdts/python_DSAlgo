def minimizeSystemCost(k, machines):
    #k=3
    #machines = [3,9,4,2,16]
    #print(f"machines: {machines}, k: {k}")
    n = len(machines)
    
    total_cost = sum(abs(machines[i] - machines[i+1]) for i in range(n-1))
    print(f"total_cost: {total_cost}")
    diffs = [abs(machines[i] - machines[i+1]) for i in range(n-1)]
    print(f"diffs: {diffs}")
    prefix_sum = [0]*(n) 
    
    for i in range(n-1):
        prefix_sum[i+1] = prefix_sum[i] + diffs[i]
    print(f"prefix_sum: {prefix_sum}")
    min_cost = float('inf')
    
    for i in range(n-k+1):
        print(f"for i: {i}")
        #window_cost = sum(abs(machines[j] - machines[j+1]) for j in range(i, i+k-1))
        window_cost = prefix_sum[i+k-1] - prefix_sum[i]
        print(f"window_cost: {window_cost}")
        bound_cost = 0
        if i > 0:
            bound_cost += abs(machines[i-1] - machines[i])
        if i+k < n:
            bound_cost += abs(machines[i+k-1] - machines[i+k])
        print(f"bound_cost: {bound_cost}")
        
        reconn_cost = 0
        if i > 0 and i+k < n:
            reconn_cost = abs(machines[i-1] - machines[i+k])
        print(f"reconn_cost: {reconn_cost}")
        new_cost = total_cost - window_cost - bound_cost + reconn_cost
        print(f"new_cost: {new_cost}")
        min_cost = min(min_cost, new_cost)
    
    return min_cost


    def findMinimumMachinesSize(machineCapacity):
        
        def efficiency(seq):
            return sum(abs(seq[i] - seq[i+1]) for i in range(len(seq) - 1))
        
        original_eff = efficiency(machineCapacity)
        machines = len(machineCapacity)

        result = [machineCapacity[0]]

        for i in range(1, machines):
            result.append(machineCapacity[i])
            
            while len(result) >= 3:
                a, b, c = result[-3], result[-2], result[-1]
                if abs(a - b) + abs(b - c) == abs(a - c):
                    result.pop(-2)
                else:
                    break

        if efficiency(result) == original_eff:
            return len(result)
        else:
            return machines