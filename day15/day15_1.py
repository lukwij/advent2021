# day15_1.py
import heapq


def get_risk_levels(filename: str):
    risk_levels = []
    with open(filename) as f:
        for y, line in enumerate(f):
            risk_levels.append([((y, x), int(risk)) for x, risk in enumerate(line.strip())])
    return risk_levels


def find_safe_path(filename: str):
    risk_level_map = get_risk_levels(filename)
    adj = get_adjacencies(risk_level_map)
    target = (len(risk_level_map) - 1, len(risk_level_map[0]) - 1)
    parent, d = dijkstra(adj, (0, 0), target)
    print(f"parent: {parent}\nd: {d}")
    return d[target]


def get_adjacencies(risk_level_map):
    adj = {}
    for y, row in enumerate(risk_level_map):
        for x, risk_level in enumerate(row):
            adj[(y, x)] = []
            if y > 0:
                adj[(y, x)].append(risk_level_map[y - 1][x])
            if x < len(row) - 1:
                adj[(y, x)].append(risk_level_map[y][x + 1])
            if y < len(risk_level_map) - 1:
                adj[(y, x)].append(risk_level_map[y + 1][x])
            if x > 0:
                adj[(y, x)].append(risk_level_map[y][x - 1])
    return adj


def dijkstra(adj, start, target):
    d = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    visited = set()
    while pq:
        du, u = heapq.heappop(pq)
        if u in visited:
            continue
        if u == target:
            break
        visited.add(u)
        for v, weight in adj[u]:
            if v not in d or d[v] > du + weight:
                d[v] = du + weight
                parent[v] = u
                heapq.heappush(pq, (d[v], v))

    return parent, d


if __name__ == "__main__":
    print(find_safe_path("input.txt"))
