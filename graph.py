import string
from typing import Union

GraphDict = dict[Union[int, str], list[int | str]]
GraphDictWeight = dict[Union[int, str], list[list[int | str]]]


class Graph:
    """
    Класс Graph используется для работы с взвешенным неориентированным графом

    Атрибуты
        graph_dict: dict
            словарь графа
        weighted_graph: bool
            флаг взвешенного графа
    """

    def __init__(self, graph_dict: GraphDict | GraphDictWeight = {}, weighted_graph: bool | None = None) -> None:
        """
        Метод инициализации класса графа
        Если graph_dict не подается, то граф пустой
        Если weighted_graph не подается, то все весы ребер у графа - 1


        Параметры
        ---------
        graph_dict: dict
            словарь графа
        weighted_graph: bool
            флаг взвешенного графа


        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(graph) # Граф с 3 вершинами и 6 ребрами
        """


        self._graph_dict: GraphDict | GraphDictWeight = graph_dict.copy()


        # проверка на взвешенный или невзвешенный граф
        if weighted_graph is None:
            if self._graph_dict:
                if type(self._graph_dict[list(self._graph_dict.keys())[0]][0]) == list:
                    weighted_graph = True

        # если нужно, преобразование в взвешенный
        if not weighted_graph:
            self.__convert_to_weighted_graph()

        self.curr_idx = 0


    def get_graph_weighted(self) -> GraphDictWeight:
        """
        Метод для получения взвешенного графа
        """

        return self._graph_dict
    

    def get_graph_not_weight(self) -> GraphDict:
        """
        Метод для получения невзвешенного графа

        Возвращает невзвешенный граф (GraphDict)

        Пример использования:

            graph = Graph({'A': [['B', 1], ['C', 1]],
                           'B': [['A', 1], ['C', 1]],
                           'C': [['A', 1], ['B', 1]]})
            print(graph.get_graph_not_weight())

            # {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        """

        return {i: [el[0] for el in self._graph_dict[i]] for i in self._graph_dict}


    def __convert_to_weighted_graph(self) -> None:
        """
        Метод реобразования из невзшенного в взвешенный граф (self._graph_dict) с весом ребра 1

        Используется только в методах класса

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(graph._graph_dict)

            # {'A': [['B', 1], ['C', 1]], 'B': [['A', 1], ['C', 1]], 'C': [['A', 1], ['B', 1]]}
        """
        for v in self._graph_dict:
            self._graph_dict[v] = [[j, 1] for j in self._graph_dict[v]]


    def find_vertex_list(self, vertex: str | int, find_vertex: str | int) -> list[str | int, int] | None:
        """
        Метод нахождения вершины ([вершина, вес]) в списке вершин вершины vertex

        Параметры
        ---------
        vertex: str | int
            вершина, в списке которой ищем
        find_vertex: str | int
            вершина, которую нужно найти

        Возвращает [вершина, вес] или None

        Пример использования:

            graph = Graph({'A': [['B', 1], ['C', 1]],
                           'B': [['A', 1], ['C', 1]],
                           'C': [['A', 1], ['B', 1]]})
            print(graph.find_vertex_list('B', 'C'))

            # ['C', 1]
        """
        for el in self._graph_dict[vertex]:
            if el[0] == find_vertex:
                return el

        return None


    def get_vertices(self) -> list[str, int]:
        """
        Метод получения всех вершин графа

        Возвращает список вершин

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.get_vertices()

            # ['A', 'B', 'C']
        """

        return [vertex for vertex in self._graph_dict]


    def get_edges(self, weights: bool = True) -> list[int | str] | list[int | str]:
        """
        Метод получения всех ребер графа

        Параметры
        ---------
        weights: bool
            по умолчанию True
            возвращение с весами или нет


        Возвращает список из ребер в виде [[['A', 'B'], 1], [['B', 'C'], 1]]
        Если невзвешенный - [['A', 'B'], ['B', 'C']]


        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.get_edges()

            # [[['A', 'B'], 1], [['A', 'C'], 1], [['B', 'A'], 1], [['B', 'C'], 1], [['C', 'A'], 1], [['C', 'B'], 1]]
        """

        edges_list: list = list()

        for start_vertex in self._graph_dict:
            for value_vertex in self._graph_dict[start_vertex]:
                end_vertex, weight = value_vertex
                if weights:
                    edges_list.append([[start_vertex, end_vertex], weight])
                else:
                    edges_list.append([start_vertex, end_vertex])
        return sorted(edges_list)


    def add_vertex(self, vertex: str | int) -> None:
        """
        Метод добавления вершины

        Параметры
        ---------
        vertex: str | int
            добавляемая вершина

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.add_vertex('D') # None
        """

        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []


    def add_vertices(self, vertices: list[str | int]) -> None:
        """
        Метод добавления нескольких вершин

        Параметры
        ---------
        vertices: list[str, int]
            список из добавляемых вершин

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.add_vertices(['D', 'E', 'F']) # None
        """

        for vertex in vertices:
            self.add_vertex(vertex)


    def delete_vertex(self, vertex_remove: str | int) -> None:
        """
        Метод удаления вершины

        Параметры
        ---------
        vertex_remove: str | int
            удаляемая вершина

        Возвращает None
        Вызывает исключение, в случае если вершина не найдена

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.delete_vertex('A') # None
        """

        if vertex_remove not in self._graph_dict:
            raise Exception("Вершина ис нот найти", "Нету такой вершины")

        for vertex in self._graph_dict:
            vertex_data = self.find_vertex_list(vertex, vertex_remove)
            if vertex_data:
                self._graph_dict[vertex].remove(vertex_data)

        self._graph_dict.pop(vertex_remove)


    def delete_vertices(self, vertices_remove: list[str | int]) -> None:
        """
        Метод удаления вершин

        Параметры
        ---------
        vertices_remove: str | int
            удаляемые вершины

        Возвращает None
        Вызывает исключение, в случае если какая-либо вершина из списка не найдена


        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.delete_vertices(['B', 'C']) # None
        """

        for vertex in vertices_remove:
            self.delete_vertex(vertex)


    def add_edge(self, start_vertex: str | int, end_vertex: str | int, weight: int = 1) -> None:
        """
        Метод добавления ребра

        Параметры
        ---------
        start_vertex: str | int
            начальная вершина ребра
        start_vertex: str | int
            начальная вершина ребра
        weight: int
            вес ребра

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.add_edge('C', 'D', 3) # None
        """

        if start_vertex not in self._graph_dict: self.add_vertex(start_vertex)
        if end_vertex not in self._graph_dict: self.add_vertex(end_vertex)

        if not self.find_vertex_list(start_vertex, end_vertex):
            self._graph_dict[start_vertex].append([end_vertex, weight])
        if not self.find_vertex_list(end_vertex, start_vertex):
            self._graph_dict[end_vertex].append([start_vertex, weight])


    def add_edges(self, edges: list[list[str | int, int]]) -> None:
        """
        Метод добавления ребер

        Параметры
        ---------
        edges: list[list[str | int, int]]
            список добавляемых ребер

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.add_edges(['C', 'D', 3], ['D', 'A', 2]) # None
        """

        for edge in edges:
            self.add_edge(*edge)


    def delete_edge(self, start_vertex: str | int, end_vertex: str | int) -> None:
        """
        Метод удаления ребра

        Параметры
        ---------
        start_vertex: str | int
            начальная вершина ребра
        start_vertex: str | int
            начальная вершина ребра

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.delete_edge('A', 'B') # None
        """

        if start_vertex in self._graph_dict and end_vertex in self._graph_dict:
            self._graph_dict[start_vertex].remove(self.find_vertex_list(start_vertex, end_vertex))
            self._graph_dict[end_vertex].remove(self.find_vertex_list(end_vertex, start_vertex))


    def delete_edges(self, edges_remove: list[list[str | int, int]]) -> None:
        """
        Метод удаления ребер

        Параметры
        ---------
        edges: list[list[str | int, int]]
            список удаляемых ребер

        Возвращает None

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            graph.delete_edges([['A', 'B'], ['B', 'C']]) # None
        """

        for edge in edges_remove:
            self.delete_edge(*edge)


    # def show(self) -> None:
    #     """Показ графа визуально"""
    #     G = nx.Graph(self._graph_dict)
    #     pos = nx.spring_layout(G)
    #
    #     nx.draw(G, pos)
    #     nx.draw_networkx_labels(G, pos)
    #     plt.show()


    def is_subgraph(self, subgraph: GraphDict | GraphDictWeight) -> bool:
        """
        Метод проверки графа на подграф

        Параметры
        ---------
        subgraph: GraphDict | GraphDictWeight
            граф, который проверяем на подграф данному

        Возвращает bool (True или False)
        """

        for el in Graph(subgraph).get_edges(weights=False):
            if el not in self.get_edges(weights=False):
                return False
        return True


    def dfs(self, start_node: str | int) -> list[str | int]:
        """
        Метод прохода в глубину

        Параметры
        ---------
        start_node: str | int
            стартовая вершина

        Возвращает генератор с вершинами list[str | int], которые прошли

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(list(graph.dfs('A')))  # ['A', 'B', 'C']
        """

        visited_nodes = set()
        stack = [start_node]

        # Повторяем пока стек не будет пустым (не закончатся вершины)
        while stack:
            # Извлекаем текущую вершину из стека (берем последний элемент)
            current_node = stack.pop()
            # Проверяем на вхождение в посещенные вершины
            if current_node not in visited_nodes:
                visited_nodes.add(current_node)
                yield current_node

            stack.extend(set(self.get_graph_not_weight()[current_node]) - visited_nodes)


    def bfs(self, start_node: str | int) -> list[str | int]:
        """
        Метод прохода в ширину

        Параметры
        ---------
        start_node: str | int
            стартовая вершина

        Возвращает генератор с вершинами list[str | int], которые прошли

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(list(graph.bfs('A')))  # ['A', 'B', 'C']
        """

        visited_nodes = set()
        queue_nodes = [start_node]
        # Обходим граф, пока очередь не будет пустая
        while queue_nodes:
            current_node = queue_nodes.pop(0)

            if current_node not in visited_nodes:
                visited_nodes.add(current_node)

                queue_nodes.extend(set(self.get_graph_not_weight()[current_node]) - visited_nodes)
                yield current_node


    def dfs_paths(self, start_node: str | int, finish_node: str | int):
        """
        Метод поиска путей в глубину

        Параметры
        ---------
        start_node: str | int
            стартовая вершина
        finish_node: str | int
            конечная вершина

        Возвращает генератор с путями

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                   'B': ['A', 'C'],
                   'C': ['A', 'B']})
            print(list(graph.dfs_paths('A', 'C')))

            # [['A', 'C'], ['A', 'B', 'C']]
        """
        stack: list = [(start_node, [start_node])]

        while stack:
            current_node, path = stack.pop()

            for neighbor_node in set(self.get_graph_not_weight()[current_node]) - set(path):
                if neighbor_node == finish_node:
                    yield path + [neighbor_node]
                else:
                    stack.append((neighbor_node, path + [neighbor_node]))


    def bfs_paths(self, start_node: str | int, finish_node: str | int):
        """
        Метод поиска путей в ширину

        Параметры
        ---------
        start_node: str | int
            стартовая вершина
        finish_node: str | int
            конечная вершина

        Возвращает генератор с путями

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                   'B': ['A', 'C'],
                   'C': ['A', 'B']})
            print(list(graph.bfs_paths('A', 'C')))

            # [['A', 'C'], ['A', 'B', 'C']]
        """
        queue_nodes = [(start_node, [start_node])]

        while queue_nodes:

            current_node, path = queue_nodes.pop(0)
            for neighbor_node in set(self.get_graph_not_weight()[current_node]) - set(path):
                if neighbor_node == finish_node:
                    yield path + [neighbor_node]
                else:
                    queue_nodes.append((neighbor_node, path + [neighbor_node]))


    def shortest_path(self, start_node: str | int, finish_node: str | int) -> list[str| int]:
        """
        Метод поиска кратчайшего пути

        Параметры
        ---------
        start_node: str | int
            стартовая вершина
        finish_node: str | int
            конечная вершина

        Возвращает список кратчайшего пути

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                   'B': ['A', 'C'],
                   'C': ['A', 'B']})
            print(list(graph.shortest_path('A', 'C')))

            # ['A', 'C']
        """

        try:
            return next(self.bfs_paths(start_node, finish_node))
        except StopIteration:
            return None


    def get_degree_vertex(self, vertex: str | int) -> int:
        """
        Метод получения степени вершины

        Параметры
        ---------
        vertex: str | int
            вершина, у которой нужно узнать степень


        Возвращает int

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(graph.get_degree_vertex('B')) # 2
        """
        return len(self._graph_dict[vertex])


    def is_isomorph(self, graph_isomorph: GraphDict | GraphDictWeight) -> bool:
        """
        Метод проверки графа на изоморфность

        Параметры
        ---------
        graph_isomorph: GraphDict | GraphDictWeight
            граф, который проверяем на изоморфность с данным

        Возвращает bool

        Пример использования:

            graph = Graph({
                'A': ['B', 'C'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F'],
                'D': ['B'],
                'E': ['B', 'F'],
                'F': ['E', 'C'],
            })

            isomorph_graph = Graph({
                'A': ['E', 'D', 'F'],
                'B': ['F', 'C'],
                'C': ['B', 'D', 'E'],
                'D': ['A', 'C', 'E', 'F'],
                'E': ['D', 'C', 'A'],
                'F': ['A', 'D', 'B']
            })

            print(graph.is_isomorph(isomorph_graph)) # True
        """

        graph_isomorph = Graph(graph_isomorph)

        for i in self.get_vertices():
            if set(self.get_vertices()) - set(self.get_graph_not_weight()[i]) - set(i) \
                    != set(graph_isomorph.get_graph_not_weight()[i]):
                return False

        return True


    def get_adjacency_vertices(self, vertex: str | int) -> list:
        """
        Метод получения смежных вершин

        Параметры
        ---------
        vertex: str | int
            вершина, у которой нужно узнать смежные вершины

        Возвращает list

        Пример использования:

            graph = Graph({'A': ['B', 'C'],
                           'B': ['A', 'C'],
                           'C': ['A', 'B']})
            print(graph.get_adjacency_vertices('B')) # ['A', 'C']
        """

        return [v[0] for v in self._graph_dict[vertex]]


    def get_addition_graph(self) -> GraphDict:
        """
        Метод получения дополнение простого графа

        Возвращает GraphDict

        Пример использования:

            graph = Graph({'A': ['C'],
                           'B': ['C'],
                           'C': ['A', 'B']})
            print(graph.get_addition_graph())

            # {'A': ['B'], 'B': ['A'], 'C': []}
        """

        graph_temp = {}
        vertices = self.get_vertices()

        for vertex in vertices:
            graph_temp[vertex] = list(set(vertices) - set(self.get_graph_not_weight()[vertex]) - set(vertex))

        return graph_temp


    def is_addition_graph(self, graph_addition: dict) -> bool:
        """
        Метод проверки графа на дополняюший граф

        Параметры
        ---------
        graph_addition: GraphDict
            граф, который проверяем на дополнение с данным

        Возвращает bool

        Пример использования:

            graph = Graph({'A': ['C'],
                           'B': ['C'],
                           'C': ['A', 'B']})
            print(graph.is_addition_graph({'A': ['B'], 'B': ['A'], 'C': []})) # True
        """
        graph_temp = self.get_graph_not_weight()
        vertices = [v for v in graph_temp]

        for vertex in vertices:
            if set(graph_addition[vertex]) != (set(vertices) - set(graph_temp[vertex]) - set(vertex)):
                return False

        return True


    def get_adjacency_matrix(self) -> list[list[int]]:
        """
        Метод получения матрицы смежности

        Возвращает list[list[int]]

        Пример использования:

            graph = {
                'A': ['B', 'C'],
                'B': ['A', 'D', 'E'],
                'C': ['A', 'F'],
                'D': ['B'],
                'E': ['B', 'F'],
                'F': ['E', 'C'],
            }
            print(Graph(graph).get_adjacency_matrix())

            # [[0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 1, 0]]
        """

        matrix = []
        temp_list = []

        for v1 in self.get_vertices():
            for v2 in self.get_vertices():
                v_res = self.find_vertex_list(v1, v2)
                if v_res:
                    temp_list.append(v_res[1])
                else:
                    temp_list.append(0)

            matrix.append(temp_list)
            temp_list = []

        return matrix


    def create_from_adjacency_matrix(self, matrix: list[list[int]]):
        """
        Метод создания графа из матрицы смежности

        Параметры
        ---------
        matrix: list[list[int]]
            матрица смежности

        Возвращает Graph

        Пример использования:


            print(Graph().create_from_adjacency_matrix([[0, 1, 1, 0, 0, 0],
                                                        [1, 0, 0, 1, 1, 0],
                                                        [1, 0, 0, 0, 0, 1],
                                                        [0, 1, 0, 0, 0, 0],
                                                        [0, 1, 0, 0, 0, 1],
                                                        [0, 0, 1, 0, 1, 0]]))

            # Граф с 6 вершинами и 12 ребрами
        """

        vertices = list(string.ascii_uppercase)[:len(matrix)]

        self._graph_dict = {}
        self.add_vertices(vertices)

        for vertex_idx in range(len(matrix)):
            vertex = matrix[vertex_idx]
            for edge_idx in range(len(vertex)):
                if vertex[edge_idx]:
                    self.add_edge(vertices[vertex_idx], vertices[edge_idx], vertex[edge_idx])

        return self


    def __str__(self):
        return f"Граф с {len(self.get_vertices())} вершинами и {len(self.get_edges())} ребрами"


    def __iter__(self):
        return self


    def __next__(self):
        if len(self.get_vertices()) == self.curr_idx:
            raise StopIteration

        curr = self.get_vertices()[self.curr_idx]
        self.curr_idx += 1
        return curr