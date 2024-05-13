def solution(name):
    spellMove = 0
    cursorMove = len(name) - 1

    for i, spell in enumerate(name):
        spellMove += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        cursorMove = min([cursorMove, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    return spellMove + cursorMove

name = "JAN"
print(solution(name))