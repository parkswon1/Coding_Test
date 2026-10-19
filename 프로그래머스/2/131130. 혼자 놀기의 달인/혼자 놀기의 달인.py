def solution(cards):
    answer = [0]
    visited = set()
    for i in range(len(cards)):
        node = i + 1
        count = 0
        while(1):
            if node not in visited:
                visited.add(node)
                nextNode = cards[node - 1]
                node = nextNode
                count += 1
            else:
                break
        answer.append(count)
    
    answer.sort()
    return answer[-1] * answer[-2]