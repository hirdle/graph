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


    def updateGraph(self):
        self.deleteVertexSelect.clear()
        self.deleteVertexSelect.addItems(self._graph.get_vertices())
        self.deleteStartEdgeSelect.addItems(self._graph.get_vertices())
        self.deleteEndEdgeSelect.addItems(self._graph.get_vertices())
        self.plot_graph()


    def importGraph(self):
        fileName = QFileDialog.getOpenFileName(self, caption="Льал")
        if fileName[0]:
            with open(fileName[0], 'r') as file:
                self._graph.create_from_adjacency_matrix(
                    matrix=[list(map(int, line.split(' '))) for line in file.readlines()]
                )
                self.updateGraph()


    def exportGraph(self):
        fileName = QFileDialog.getSaveFileName(self, caption="Льал")
        if fileName[0]:
            with open(fileName[0], 'w') as file:
                for row in self._graph.get_adjacency_matrix():
                    print(*row, file=file)


    def add_vertex(self):
        self._graph.add_vertex(self.vertexAddInput.text())
        self.vertexAddInput.clear()
        self.updateGraph()

    
    def delete_vertex(self):
        self._graph.delete_vertex(self.deleteVertexSelect.currentText())
        self.updateGraph()

    def delete_edge(self):
        self._graph.delete_edge(self.deleteStartEdgeSelect.currentText(), self.deleteEndEdgeSelect.currentText())
        self.deleteStartEdgeSelect.clear()
        self.deleteEndEdgeSelect.clear()
        self.updateGraph()



    def add_edge(self):
        self._graph.add_edge(self.startEdgeAddInput.text(), self.endEdgeAddInput.text())
        self.startEdgeAddInput.clear()
        self.endEdgeAddInput.clear()
        self.updateGraph()


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

        # Составление графа в зависимости от его типа
        if type(_graph_dict[list(_graph_dict.keys())[0]][0]) == list:

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
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec())
