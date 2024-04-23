"""
제한사항
scoville개수가 2이상 1000000 이하
ksms 0이상 1000000000이하
원소는 0이상 1000000이하
스코빌 지수를 K이상 못만드는 경우 -1 출력 (0이 2개 이상이면 불가 두번째로 낮은 스코빌 지수가 항상 0 * 2 = 0 이 됨으로)

구현사항
1. 스코빌 지수를 정렬 낮은 값부터 뽑아내기 위함
2. 정렬을 오름차순 heapq에다가 넣어서 값이 자동으로 정렬되도록 만들자
3 - 1. heapq의 처음 값을 뽑았을때 K보다 높거나 같다면 break
3 - 2 - 1. heapq의 처음 값을 뽑았을때 k보다 낮다면
3 - 2 - 2. 하나 더 뽑아서 * 2 + 처음 뽑은 값 (만약 하나 더뽑은것이 0이라면 break)
3 - 2 - 3. 2번에서 나온 값 다시 heapq에 넣기
4. 3-1 부터 반복
5. scovile에 남은 값중 가장 낮은 값이 K보다 큰지본다
5 - 1. 크다면 answer리턴
5 - 2. 작다면 -1 리턴
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(len(scoville) > 1):
        first = heapq.heappop(scoville)
        if first >= K:
            break
        else:
            second = heapq.heappop(scoville)
            if second == 0:
                break
            else:
                answer += 1
                heapq.heappush(scoville, first + (second * 2))

    if scoville[0] >= K:
        return answer
    else:
        return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 4
print(solution(scoville,K))