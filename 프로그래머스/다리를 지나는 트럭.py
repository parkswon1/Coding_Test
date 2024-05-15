from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    N = len(truck_weights)
    bridge = deque([0]*bridge_length)
    nowWeight = 0
    stopedTruckCount = 0
    index = 0

    while(1):
        if N == stopedTruckCount:
            break;
        now = bridge.popleft()
        if now != 0:
            stopedTruckCount += 1
            nowWeight -= now

        if nowWeight + truck_weights[index] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights[index])
            nowWeight += truck_weights[index]
            if index < N - 1:
                index += 1

        answer += 1

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))