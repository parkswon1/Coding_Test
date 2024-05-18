def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    rank = [0] * n

    total_cost = 0
    edges_used = 0

    for cost in costs:
        island1, island2, bridge_cost = cost

        if find(parent, island1) != find(parent, island2):
            union(parent, rank, island1, island2)
            total_cost += bridge_cost
            edges_used += 1

            if edges_used == n - 1:
                break

    return total_cost
