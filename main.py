from PyQt6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx
import sys
from design import Ui_MainWindow
from graph import Graph 


class GraphWindow(QMainWindow, Ui_MainWindow):
    """Класс окна приложения"""

    def __init__(self):
        """Инициализация"""

        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Приложение для работы с графами КапиГраф")
        self.init_canvas()

        self._graph = Graph({
            'A': [['B', 1], ['C', 5]],
            'B': [['A', 1], ['C', 9]],
            'C': [['A', 10], ['B', 5]]
        })
        
        self.updateGraph()

        self.vertexAddBtn.clicked.connect(self.add_vertex)
        self.edgeAddBtn.clicked.connect(self.add_edge)
        self.vertexDeleteBtn.clicked.connect(self.delete_vertex)
        self.edgeDeleteBtn.clicked.connect(self.delete_edge)

        self.exportBtn.clicked.connect(self.exportGraph)
        self.importBtn.clicked.connect(self.importGraph)
        self.bfsGetBtn.clicked.connect(self.show_bfs_paths)
        self.dfsGetBtn.clicked.connect(self.show_dfs_paths)
        self.exportInput.addItems(['Сохранение в картинку', 'Сохранить в матрицу смежности'])


    def updateGraph(self):
        """Обновление графа"""

        self.deleteVertexSelect.clear()
        self.deleteStartEdgeSelect.clear()
        self.deleteEndEdgeSelect.clear()
        self.deleteVertexSelect.addItems(self._graph.get_vertices())
        self.deleteStartEdgeSelect.addItems(self._graph.get_vertices())
        self.deleteEndEdgeSelect.addItems(self._graph.get_vertices())
        self.plot_graph()


    def importGraph(self):
        """Импорт графа"""

        fileName = QFileDialog.getOpenFileName(self, caption="Выбор графа", filter='*.txt')
        if fileName[0]:
            with open(fileName[0], 'r') as file:
                try:
                    self._graph.create_from_adjacency_matrix(
                        matrix=[list(map(int, line.split(' '))) for line in file.readlines()]
                    )
                    self.updateGraph()
                    QMessageBox.information(self, "Успешно", "Граф успешно импортирован")

                except:
                    QMessageBox.warning(self, "Ошибка", "Неверные данные в файле")


    def exportGraph(self):
        """Экспорт графа"""

        match self.exportInput.currentText():

            case 'Сохранение в картинку':

                fileName = QFileDialog.getSaveFileName(self, 'Сохранение графа в картинку', 'graph.jpg', filter=self.tr(".jpg"))
                if fileName[0]:
                    plt.savefig(fileName[0], format="JPG")
                

            case 'Сохранить в матрицу смежности':

                fileName = QFileDialog.getSaveFileName(self, 'Сохранение графа', 'graph.txt', filter=self.tr(".txt"))
                if fileName[0]:
                    with open(fileName[0], 'w') as file:
                        for row in self._graph.get_adjacency_matrix():
                            print(*row, file=file)


    def add_vertex(self):
        """Добавление вершины"""

        if self.vertexAddInput.text():
            self._graph.add_vertex(self.vertexAddInput.text())
            self.vertexAddInput.clear()
            self.updateGraph()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите вершину")

    
    def delete_vertex(self):
        """Удаление вершины"""

        if self.deleteVertexSelect.currentText():
            self._graph.delete_vertex(self.deleteVertexSelect.currentText())
            self.updateGraph()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите вершину для удаления")


    def delete_edge(self):
        """Удаление ребра"""

        if self.deleteStartEdgeSelect.currentText() and self.deleteEndEdgeSelect.currentText():
            self._graph.delete_edge(self.deleteStartEdgeSelect.currentText(), self.deleteEndEdgeSelect.currentText())
            self.deleteStartEdgeSelect.clear()
            self.deleteEndEdgeSelect.clear()
            self.updateGraph()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите вершины для удаления ребра")


    def add_edge(self):
        """"Добавление ребра"""

        if self.startEdgeAddInput.text() and self.endEdgeAddInput.text():
            self._graph.add_edge(self.startEdgeAddInput.text(), self.endEdgeAddInput.text())
            self.startEdgeAddInput.clear()
            self.endEdgeAddInput.clear()
            self.updateGraph()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите вершины для добавления ребра")


    def init_canvas(self):
        """Функция инициализации холста"""

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()

        layout.addWidget(self.canvas)
        self.graphFrame.setLayout(layout)


    def plot_graph(self):
        """Функция отрисовки взвешенного графа"""
        
        B = nx.Graph()

        _graph_dict = self._graph._graph_dict

        weight_graph = False

        try:
            weight_graph = type(_graph_dict[list(_graph_dict.keys())[0]][0]) == list
        except: pass

        # Составление графа в зависимости от его типа
        if weight_graph:

            for node, edges in _graph_dict.items():
                B.add_node(node)

                for neighbor, weight in edges:
                    B.add_node(neighbor)
                    B.add_edge(node, neighbor, weight=weight)
                
        else:

            for node, edges in _graph_dict.items():
                for neighbor in edges:
                    B.add_edge(node, neighbor)
   

        pos = nx.spring_layout(B)  # Позиционирование

        # Очистка
        self.figure.clf()
        ax = self.figure.add_subplot(111)

        # Отрисовка
        edge_labels = nx.get_edge_attributes(B, 'weight')  # Get weights for edges
        nx.draw(B, pos, with_labels=True, ax=ax)
        nx.draw_networkx_edge_labels(B, pos, edge_labels=edge_labels, ax=ax)

        self.canvas.draw()


    def show_bfs_paths(self):
        """Показать пути BFS в модальном окне"""
        
        start_vertex = self.bfsStartVertexInput.text()
        finish_vertex = self.bfsFinishVertexInput.text()  # Получаем конечную вершину
        if start_vertex and finish_vertex:
            if finish_vertex in self._graph.get_vertices():  # Проверка на существование конечной вершины
                paths = self._graph.bfs_paths(start_vertex, finish_vertex)  # Передаем конечную вершину
                # Преобразование каждого пути в строку
                paths_str = [" -> ".join(path) for path in paths]
                QMessageBox.information(self, "Пути BFS", f"Пути от {start_vertex} до {finish_vertex}:\n" + "\n".join(paths_str))
            else:
                QMessageBox.warning(self, "Ошибка", "Конечная вершина не существует в графе")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите стартовую и конечную вершину для BFS")


    def show_dfs_paths(self):
        """Показать пути DFS в модальном окне"""
        
        start_vertex = self.dfsStartVertexInput.text()
        finish_vertex = self.dfsFinishVertexInput.text()  # Получаем конечную вершину
        if start_vertex and finish_vertex:
            if finish_vertex in self._graph.get_vertices():  # Проверка на существование конечной вершины
                paths = self._graph.dfs_paths(start_vertex, finish_vertex)  # Передаем конечную вершину
                # Преобразование каждого пути в строку
                paths_str = [" -> ".join(path) for path in paths]
                QMessageBox.information(self, "Пути DFS", f"Пути от {start_vertex} до {finish_vertex}:\n" + "\n".join(paths_str))
            else:
                QMessageBox.warning(self, "Ошибка", "Конечная вершина не существует в графе")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите стартовую и конечную вершину для DFS")


if __name__ == '__main__':
    """Старт приложения"""

    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec())
