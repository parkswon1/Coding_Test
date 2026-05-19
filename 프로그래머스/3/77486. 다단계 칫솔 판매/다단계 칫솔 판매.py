def solution(enroll, referral, seller, amount):
    answer = []
    price = {"-":0}
    tree = {}
    for i in range(len(enroll)):
        price[enroll[i]] = 0
        tree[enroll[i]] = referral[i]
    
    for j in range(len(seller)):
        sell = seller[j]
        amo = amount[j] * 100
        while(1):
            give = amo // 10
            price[sell] += amo - give
            amo = give
            if tree[sell] == "-" or amo == 0:
                break
            
            sell = tree[sell]
    
    for e in enroll:
        answer.append(price[e])
    return answer