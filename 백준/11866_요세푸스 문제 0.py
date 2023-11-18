from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))

output = []

count = 0
while(len(queue) != 0):
    count += 1
    if count == K:
        count = 0
        output.append(queue.popleft())
    else:
        queue.append(queue.popleft())

print('<'+", ".join(map(str,output)) + ">")