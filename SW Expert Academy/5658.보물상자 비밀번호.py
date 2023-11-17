import heapq
T = int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    rock = input()
    numbers = set()
    for n in range(N):
        end =n+int(N/4)
        rnumber = rock[n:end]
        diff = end - N
        if diff > 0:
            rnumber = rnumber + rock[:diff]
        numbers.add(int(rnumber, 16))

    print(f'#{test_case}',heapq.nlargest(K,numbers)[-1])