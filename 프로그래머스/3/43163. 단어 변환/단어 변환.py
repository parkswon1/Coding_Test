from collections import deque

def isDiffOneWord(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
            if count > 1:
                return 0
    return 1

def solution(begin, target, words):
    answer = 0
    visited = set()
    nodes = deque([])
    nodes.append((begin, 0))
    visited.add(begin)
    
    while(nodes):
        node, count = nodes.popleft()
        if node == target:
            return count
        
        for word in words:
            if isDiffOneWord(node, word) and word not in visited:
                visited.add(word)
                nodes.append((word, count + 1))
    
    return 0