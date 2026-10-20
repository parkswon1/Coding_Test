def solution(user_id, banned_id):
    answer = set()
    visited = set()

    def match(user, banned):
        if len(user) != len(banned):
            return False

        for u, b in zip(user, banned):
            if b != '*' and u != b:
                return False

        return True

    def dfs(idx):
        if idx == len(banned_id):
            answer.add(frozenset(visited))
            return

        for user in user_id:
            if user in visited:
                continue

            if match(user, banned_id[idx]):
                visited.add(user)
                dfs(idx + 1)
                visited.remove(user)

    dfs(0)
    return len(answer)