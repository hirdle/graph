# Документация для функций класса Graph

## Список всех функций
1. `__init__(self, graph_dict: GraphDict | GraphDictWeight = {}, weighted_graph: bool | None = None) -> None`
2. `get_graph_weighted(self) -> GraphDictWeight`
3. `get_graph_not_weight(self) -> GraphDict`
4. `__convert_to_weighted_graph(self) -> None`
5. `find_vertex_list(self, vertex: str | int, find_vertex: str | int) -> list[str | int, int] | None`
6. `get_vertices(self) -> list[str, int]`
7. `get_edges(self, weights: bool = True) -> list[int | str] | list[int | str]`
8. `add_vertex(self, vertex: str | int) -> None`
9. `add_vertices(self, vertices: list[str | int]) -> None`
10. `delete_vertex(self, vertex_remove: str | int) -> None`
11. `delete_vertices(self, vertices_remove: list[str | int]) -> None`
12. `add_edge(self, start_vertex: str | int, end_vertex: str | int, weight: int = 1) -> None`
13. `add_edges(self, edges: list[list[str | int, int]]) -> None`
14. `delete_edge(self, start_vertex: str | int, end_vertex: str | int) -> None`
15. `delete_edges(self, edges_remove: list[list[str | int, int]]) -> None`
16. `is_subgraph(self, subgraph: GraphDict | GraphDictWeight) -> bool`
17. `dfs(self, start_node: str | int) -> list[str | int]`
18. `bfs(self, start_node: str | int) -> list[str | int]`
19. `dfs_paths(self, start_node: str | int, finish_node: str | int)`
20. `bfs_paths(self, start_node: str | int, finish_node: str | int)`
21. `shortest_path(self, start_node: str | int, finish_node: str | int) -> list[str| int]`
22. `get_degree_vertex(self, vertex: str | int) -> int`
23. `is_isomorph(self, graph_isomorph: GraphDict | GraphDictWeight) -> bool`
24. `get_adjacency_vertices(self, vertex: str | int) -> list`
25. `get_addition_graph(self) -> GraphDict`
26. `is_addition_graph(self, graph_addition: dict) -> bool`
27. `get_adjacency_matrix(self) -> list[list[int]]`
28. `create_from_adjacency_matrix(self, matrix: list[list[int]])`
29. `__str__(self)`
30. `__iter__(self)`
31. `__next__(self)`

## __init__(self, graph_dict: GraphDict | GraphDictWeight = {}, weighted_graph: bool | None = None) -> None
Метод инициализации класса графа. Если graph_dict не подается, то граф пустой. Если weighted_graph не подается, то все весы ребер у графа - 1.

### Параметры
- `graph_dict`: dict - словарь графа.
- `weighted_graph`: bool - флаг взвешенного графа.

### Возвращает
None

---

## get_graph_weighted(self) -> GraphDictWeight
Метод для получения взвешенного графа.

### Возвращает
Словарь, представляющий взвешенный граф.

---

## get_graph_not_weight(self) -> GraphDict
Метод для получения невзвешенного графа.

### Возвращает
Словарь, представляющий невзвешенный граф.

---

## __convert_to_weighted_graph(self) -> None
Метод преобразования из невзвешенного в взвешенный граф (self._graph_dict) с весом ребра 1.

### Возвращает
None

---

## find_vertex_list(self, vertex: str | int, find_vertex: str | int) -> list[str | int, int] | None
Метод нахождения вершины ([вершина, вес]) в списке вершин вершины vertex.

### Параметры
- `vertex`: str | int - вершина, в списке которой ищем.
- `find_vertex`: str | int - вершина, которую нужно найти.

### Возвращает
Список [вершина, вес] или None.

---

## get_vertices(self) -> list[str, int]
Метод получения всех вершин графа.

### Возвращает
Список вершин.

---

## get_edges(self, weights: bool = True) -> list[int | str] | list[int | str]
Метод получения всех ребер графа.

### Параметры
- `weights`: bool - по умолчанию True, возвращение с весами или нет.

### Возвращает
Список из ребер.

---

## add_vertex(self, vertex: str | int) -> None
Метод добавления вершины.

### Параметры
- `vertex`: str | int - добавляемая вершина.

### Возвращает
None

---

## add_vertices(self, vertices: list[str | int]) -> None
Метод добавления нескольких вершин.

### Параметры
- `vertices`: list[str, int] - список из добавляемых вершин.

### Возвращает
None

---

## delete_vertex(self, vertex_remove: str | int) -> None
Метод удаления вершины.

### Параметры
- `vertex_remove`: str | int - удаляемая вершина.

### Возвращает
None

---

## delete_vertices(self, vertices_remove: list[str | int]) -> None
Метод удаления вершин.

### Параметры
- `vertices_remove`: list[str | int] - удаляемые вершины.

### Возвращает
None

---

## add_edge(self, start_vertex: str | int, end_vertex: str | int, weight: int = 1) -> None
Метод добавления ребра.

### Параметры
- `start_vertex`: str | int - начальная вершина ребра.
- `end_vertex`: str | int - конечная вершина ребра.
- `weight`: int - вес ребра.

### Возвращает
None

---

## add_edges(self, edges: list[list[str | int, int]]) -> None
Метод добавления ребер.

### Параметры
- `edges`: list[list[str | int, int]] - список добавляемых ребер.

### Возвращает
None

---

## delete_edge(self, start_vertex: str | int, end_vertex: str | int) -> None
Метод удаления ребра.

### Параметры
- `start_vertex`: str | int - начальная вершина ребра.
- `end_vertex`: str | int - конечная вершина ребра.

### Возвращает
None

---

## delete_edges(self, edges_remove: list[list[str | int, int]]) -> None
Метод удаления ребер.

### Параметры
- `edges_remove`: list[list[str | int, int]] - список удаляемых ребер.

### Возвращает
None

---

## is_subgraph(self, subgraph: GraphDict | GraphDictWeight) -> bool
Метод проверки графа на подграф.

### Параметры
- `subgraph`: GraphDict | GraphDictWeight - граф, который проверяем на подграф данному.

### Возвращает
bool (True или False).

---

## dfs(self, start_node: str | int) -> list[str | int]
Метод прохода в глубину.

### Параметры
- `start_node`: str | int - стартовая вершина.

### Возвращает
Генератор с вершинами list[str | int], которые прошли.

---

## bfs(self, start_node: str | int) -> list[str | int]
Метод прохода в ширину.

### Параметры
- `start_node`: str | int - стартовая вершина.

### Возвращает
Генератор с вершинами list[str | int], которые прошли.

---

## dfs_paths(self, start_node: str | int, finish_node: str | int)
Метод поиска путей в глубину.

### Параметры
- `start_node`: str | int - стартовая вершина.
- `finish_node`: str | int - конечная вершина.

### Возвращает
Генератор с путями.

---

## bfs_paths(self, start_node: str | int, finish_node: str | int)
Метод поиска путей в ширину.

### Параметры
- `start_node`: str | int - стартовая вершина.
- `finish_node`: str | int - конечная вершина.

### Возвращает
Генератор с путями.

---

## shortest_path(self, start_node: str | int, finish_node: str | int) -> list[str| int]
Метод поиска кратчайшего пути.

### Параметры
- `start_node`: str | int - стартовая вершина.
- `finish_node`: str | int - конечная вершина.

### Возвращает
Список кратчайшего пути.

---

## get_degree_vertex(self, vertex: str | int) -> int
Метод получения степени вершины.

### Параметры
- `vertex`: str | int - вершина, у которой нужно узнать степень.

### Возвращает
int - степень вершины.

---

## is_isomorph(self, graph_isomorph: GraphDict | GraphDictWeight) -> bool
Метод проверки графа на изоморфность.

### Параметры
- `graph_isomorph`: GraphDict | GraphDictWeight - граф, который проверяем на изоморфность с данным.

### Возвращает
bool.

---

## get_adjacency_vertices(self, vertex: str | int) -> list
Метод получения смежных вершин.

### Параметры
- `vertex`: str | int - вершина, у которой нужно узнать смежные вершины.

### Возвращает
Список смежных вершин.

---

## get_addition_graph(self) -> GraphDict
Метод получения дополнение простого графа.

### Возвращает
GraphDict.

---

## is_addition_graph(self, graph_addition: dict) -> bool
Метод проверки графа на дополняющий граф.

### Параметры
- `graph_addition`: GraphDict - граф, который проверяем на дополнение с данным.

### Возвращает
bool.

---

## get_adjacency_matrix(self) -> list[list[int]]
Метод получения матрицы смежности.

### Возвращает
list[list[int]] - матрица смежности.

---

## create_from_adjacency_matrix(self, matrix: list[list[int]])
Метод создания графа из матрицы смежности.

### Параметры
- `matrix`: list[list[int]] - матрица смежности.

### Возвращает
Graph - созданный граф.

---

## __str__(self)
Метод для строкового представления графа.

### Возвращает
Строку с информацией о графе.

---

## __iter__(self)
Метод для итерирования по графу.

### Возвращает
Итератор.

---

## __next__(self)
Метод для получения следующей вершины.

### Возвращает
Следующую вершину или вызывает StopIteration.

