"""
app

batch??

list(RequestResponse)
streaming

many lists

global

1, 2, 3
s  f   f
t1 t2 t3

tot= 3
suc=1
sum times = 6
avg= sum times / total

total = prevtot + new one

"""

class RequestResponse:
    
    def __init__(self, action: str, user_id: str, success: bool, duration_in_milliseconds: float):
        self.acton = action
        self.user_id = user_id
        self.success = success
        self.duration_in_milliseconds = duration_in_milliseconds

#dict {action_id, Metrics_Holder}
class Metrics_Holder:
    #dict
    def __init__(self, total_request: int, total_success: int, sum_times: float):
        self.total_request = total_request
        self.total_success = total_success
        self.sum_times = sum_times

def get_metrics(request_responses, metrics_holder):
    total_req_batch = len(request_responses)
    total_success_batch = 0
    sum_times_batch = 0
    
    for req_resp in request_responses:
        if req_resp.success:
            total_success_batch+=1
        sum_times_batch+= req_resp.duration_in_milliseconds
        
    metrics_holder.total_request+= total_req_batch
    metrics_holder.total_success+= total_success_batch
    metrics_holder.sum_times+=sum_times_batch

req1 = RequestResponse("ac1", "usr1", True, 1)
req2 = RequestResponse("ac2", "usr2", False, 2)
req3 = RequestResponse("ac3", "usr3", False, 3)

metrics_holder = Metrics_Holder(0,0,0)

get_metrics([req1, req2, req3], metrics_holder)

print(f"total_request: {metrics_holder.total_request}")
print(f"total_success: {metrics_holder.total_success}")
print(f"avg_request: {metrics_holder.sum_times/metrics_holder.total_request}")

assert metrics_holder.total_request == 3

get_metrics([req1, req2, req3], metrics_holder)

print(f"total_request: {metrics_holder.total_request}")
print(f"total_success: {metrics_holder.total_success}")
print(f"avg_request: {metrics_holder.sum_times/metrics_holder.total_request}")

assert metrics_holder.total_request == 6

# Your code
print("Implement the answer to the question here")
