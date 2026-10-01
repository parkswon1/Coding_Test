def solution(word):
    stack = [""]
    move = ['U', 'O', 'I', 'E', 'A']
    count = 0

    while stack:
        w = stack.pop()

        if w:
            count += 1

        if w == word:
            return count

        if len(w) == 5:
            continue

        for m in move:
            stack.append(w + m)