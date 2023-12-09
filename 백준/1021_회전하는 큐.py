import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

queue1 = deque(i for i in range(1,N+1))
queue2 = deque(i for i in range(1,N+1))

output = 0
for m in range(M):
    count1 = 0
    while(1):
        if queue1[0] == numbers[m]:
            break
        queue1.append(queue1.popleft())
        count1 += 1
    queue1.popleft()
    count2 = 0
    while(1):
        if queue2[0] == numbers[m]:
            break
        queue2.appendleft(queue2.pop())
        count2 += 1
    queue2.popleft()

    output += min(count2,count1)

print(output)