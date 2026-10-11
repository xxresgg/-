import heapq

graph = {
    "Дом": {"Школа": 4, "Магазин": 2},
    "Школа": {"Дом": 4, "Парк": 5, "Колледж": 8},
    "Магазин": {"Дом": 2, "Парк": 3},
    "Парк": {"Магазин": 3, "Школа": 5, "Колледж": 4},
    "Колледж": {"Школа": 8, "Парк": 4}
}

start = "Магазин"
goal = "Парк"

distances = {v: float("inf") for v in graph}
previous = {v: None for v in graph}
distances[start] = 0

queue = [(0, start)]

while queue:
    distance, vertex = heapq.heappop(queue)

    if distance > distances[vertex]:
        continue

    for neighbor, weight in graph[vertex].items():
        new_distance = distance + weight

        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous[neighbor] = vertex
            heapq.heappush(queue, (new_distance, neighbor))

path = []
vertex = goal

while vertex is not None:
    path.append(vertex)
    vertex = previous[vertex]

path.reverse()

print("Самый быстрый путь:", " -> ".join(path))
print("Время в пути:", distances[goal], "минут")