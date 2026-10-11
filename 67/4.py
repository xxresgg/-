from collections import deque

graph = {
    "Дом": ["Школа", "Парк"],
    "Школа": ["Дом", "Магазин", "Больница"],
    "Парк": ["Дом", "Кафе", "Больница"],
    "Магазин": ["Школа", "Колледж"],
    "Больница": ["Школа", "Парк", "Университет"],
    "Кафе": ["Парк", "Университет"],
    "Университет": ["Больница", "Кафе", "Колледж"],
    "Колледж": ["Магазин", "Университет"]
}

start = "Дом"
goal = "Школа"

queue = deque([start])
visited = [start]

while queue:
    vertex = queue.popleft()
    print("Проверяем:", vertex)

    if vertex == goal:
        print("Цель найдена!")
        break

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)

print("Порядок проверки:", " -> ".join(
    visited[:visited.index(goal) + 1]
))