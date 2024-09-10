import heapq
import sys

N = int(sys.stdin.readline())

maxHeapQ = []
minHeapQ = []

for i in range(N):
    num = int(sys.stdin.readline())
    if len(maxHeapQ) == len(minHeapQ) :
        heapq.heappush(maxHeapQ, -num)
    else:
        heapq.heappush(minHeapQ, num)

    if minHeapQ and minHeapQ[0] < -maxHeapQ[0]:
        maxValue = heapq.heappop(maxHeapQ)
        minValue = heapq.heappop(minHeapQ)

        heapq.heappush(maxHeapQ, -minValue)
        heapq.heappush(minHeapQ, -maxValue)

    print(-maxHeapQ[0])