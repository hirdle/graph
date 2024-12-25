from PyQt6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx
import sys
from design import Ui_MainWindow


class GraphWindow(QMainWindow, Ui_MainWindow):
    """Класс окна приложения"""

    def __init__(self):
        """Инициализация"""

        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Приложение для работы с графами КапиГраф")
        self.init_canvas()

        self.graph_dict={
            'A': [['B', 1], ['C', 1]],
            'B': [['A', 1], ['C', 9]],
            'C': [['A', 4], ['B', 5]]
        }
        
        self.plot_graph(self.graph_dict)

        # self.plot_graph(graph_dict={'A': ['B', 'C'],
        #                    'B': ['A', 'C'],
        #                    'C': ['A', 'B']})

        self.vertexAddBtn.clicked.connect(self.add_vertex)


    def add_vertex(self):
        self.graph_dict[self.vertexAddInput.text()] = []
        self.plot_graph(self.graph_dict)


    def init_canvas(self):
        """Функция инициализации холста"""

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()

        layout.addWidget(self.canvas)
        self.graphFrame.setLayout(layout)


    def plot_graph(self, graph_dict):
        """Функция отрисовки взвешенного графа"""
        B = nx.Graph()

        # Составление графа в зависимости от его типа
        if type(graph_dict[list(graph_dict.keys())[0]][0]) == list:

            for node, edges in graph_dict.items():
                B.add_node(node)

                for neighbor, weight in edges:
                    B.add_node(neighbor)
                    B.add_edge(node, neighbor, weight=weight)
                
        else:

            for node, edges in graph_dict.items():
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
