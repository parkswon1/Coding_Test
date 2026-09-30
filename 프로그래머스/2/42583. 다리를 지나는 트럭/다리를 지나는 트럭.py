from collections import deque

def solution(bridge_length, weight, truck_weights):
    t = 0
    w = 0
    bque = deque([]) #무게, 끝나는 시간
    tque = deque(truck_weights)
    while(tque):
        print(bque)
        while bque and bque[0][1] <= t:
            a, b = bque.popleft()
            w -= a
        
        if tque[0] + w <= weight:
            truck = tque.popleft()
            bque.append((truck, t + bridge_length))
            w += truck
            t += 1
            
        else:
            t = bque[0][1]
                
    return bque[-1][1] + 1