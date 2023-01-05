import sys
N,K = list(map(int, sys.stdin.readline().split()))
queue = [N]
output =[]
for i in range(1,N):
    queue.append(i)
index = K
if N == K:
    index = 0
while(1):
    output.append(queue.pop(index))
    index -= 1
    index += K
    if len(queue) == 0:
        break
    while(index >= len(queue)):
        index -= len(queue)
        
print("<", ", ".join(str(i) for i in output), ">", sep="")