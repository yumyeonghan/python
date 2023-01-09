# 무지의 먹방 라이브
import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))
    
    lenth = len(food_times)
    sum_time = 0
    previous = 0
    
    while sum_time + (q[0][0] - previous) * lenth <= k:
        value = heapq.heappop(q)[0]
        sum_time += (value - previous) * lenth
        lenth -= 1
        previous = value
    
    result = sorted(q, key = lambda x : x[1])
    return result[(k - sum_time)% lenth][1]