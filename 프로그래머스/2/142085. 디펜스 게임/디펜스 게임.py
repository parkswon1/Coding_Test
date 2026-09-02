#일단 무적권을 사용하지않고 다 맊으면서 막은 가장 큰수들을 기록하기
#병사가 부족할경우 무적권을써서 막은 수들을 다시 채우기
#무적권도다쓰고 병사도 다쓰면 마무리

import heapq

def solution(n, k, enemy):
    answer = 0
    eque = []
    for i in range(len(enemy)):
        n -= enemy[i]
        heapq.heappush(eque,-enemy[i])

        if n >= 0:
            continue
        while(k != 0 and eque and n < 0):
            k -= 1
            n += -heapq.heappop(eque)
        if n < 0:
            return i
    return len(enemy)