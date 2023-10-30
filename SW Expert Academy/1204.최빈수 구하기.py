T = int(input())

for t in range(1,T+1):
    score_list = [0]*101
    t = int(input())
    score = list((map(int, input().split())))
    
    for s in score:
        score_list[s] += 1
    max_score = max(score_list)
    
    for s in range(100,0,-1):
        if score_list[s] == max_score:
            print(f'#{t}',s)