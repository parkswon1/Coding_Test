from collections import deque
import sys
input = sys.stdin.readline

def solve() :
  N = int(input())
  coin_list = [ list(map(int, input().split())) for _ in range(N) ]    
  target_value = sum([c[0]*c[1] for c in coin_list])
  if target_value % 2 :
    return 0
  target_value //= 2

  q = deque([0])
  for i in range(N) :
    coin, cnt = coin_list[i]
    next_q = deque()
    visited = [False]*(target_value+1)
    while q :
      cur = q.popleft()
      for j in range(cur, cur+coin*cnt+1, coin) :
        if j > target_value :
          continue
        if j == target_value :
          return 1
        if not visited[j] :
          visited[j] = True
          next_q.append(j)
    q = next_q
  return 0

for _ in range(3) :
  print(solve())