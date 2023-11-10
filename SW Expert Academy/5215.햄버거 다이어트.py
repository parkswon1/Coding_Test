def cal(T,K):
    score = T
    kal = K
    for m in range(len(max_list)):
        if max_list[m][1] + K <= L:
            score = max_list[m][0] + T
            kal = max_list[m][1] + K 
            max_list.append([score,kal])
    max_list.append([T,K])
    return

test = int(input())

for t in range(1,test+1):
    N, L = map(int,input().split())
    
    max_list = []
    for i in range(N):
        T,K = map(int,input().split())
        cal(T,K)
    
    print(f"#{t}",max(max_list)[0])