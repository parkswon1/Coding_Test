a = float(input())
b = float(input())
a /= 100
b /= 100
p = "0011010100010100010"

cache = [[[None] * 20 for _ in range(20)] for _ in range(20)]


def Sol(cur, t1, t2):
    if cur == 18:
        return p[t1] == '1' or p[t2] == '1'

    if cache[cur][t1][t2] is not None:
        return cache[cur][t1][t2]

    ret = (1 - a) * (1 - b) * Sol(cur + 1, t1, t2) + \
          a * (1 - b) * Sol(cur + 1, t1 + 1, t2) + \
          (1 - a) * b * Sol(cur + 1, t1, t2 + 1) + \
          a * b * Sol(cur + 1, t1 + 1, t2 + 1)

    cache[cur][t1][t2] = ret
    return ret


print(f"{Sol(0, 0, 0):.20f}")
