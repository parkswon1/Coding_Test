def move(d, y, x):
    if d == 'U': ny, nx = y + 1, x
    elif d == 'D': ny, nx = y - 1, x
    elif d == 'R': ny, nx = y, x + 1
    elif d == 'L': ny, nx = y, x - 1
    
    if -5 <= ny <= 5 and -5 <= nx <= 5:
        return ny, nx
    return y, x

def solution(dirs):
    answerSet = set()
    y, x = 0, 0
    
    for d in dirs:
        my, mx = move(d, y, x)
        
        if (my, mx) == (y, x):
            continue

        path = tuple(sorted([(y, x), (my, mx)]))
        answerSet.add(path)
        
        y, x = my, mx
        
    return len(answerSet)