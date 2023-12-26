import sys
import heapq

T = int(sys.stdin.readline())
for t in range(T):
    K = int(sys.stdin.readline())
    line = list(map(int,sys.stdin.readline().split()))
    files = []
    while(line):
        heapq.heappush(files,line.pop())

    output = 0
    while len(files) >= 2:
        A = heapq.heappop(files)
        B = heapq.heappop(files)
        output += A + B
        heapq.heappush(files,A + B)

    print(output)