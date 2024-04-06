import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from(list(range(1, 7)))
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5), (4, 6), (5, 6)])

nx.draw(G, with_labels=True)
plt.show()

# Эксцентриситет вершин
print(f'Эксцентриситет вершин: {nx.eccentricity(G)}')

# Степени вершин
print(f'Степени вершин: {G.degree()}')

# Матрица смежности
adjacency_matrix = nx.adjacency_matrix(G)
print(f'Матрица смежности:\n{adjacency_matrix.todense()}')

# Матрица инцидентности
incidence_matrix = nx.incidence_matrix(G)
print(f'Матрица инцидентности:\n{incidence_matrix.todense()}')

# Радиус, диаметр и центр графа
print(f'Радиус: {nx.radius(G)}')
print(f'Диаметр: {nx.diameter(G)}')
print(f'Центр: {nx.center(G)}')

# Список циклов, образующих базис циклов графа
print(f'Список циклов, образующих базис циклов графа: {nx.cycle_basis(G)}')

# Набор рёбер минимальной кардинальности для разделения графа
print(f'Набор рёбер минимальной кардинальности для разделения графа: {nx.minimum_edge_cut(G)}')

# Набор вершин минимальной кардинальности для разделения графа
print(f'Набор вершин минимальной кардинальности для разделения графа: {nx.minimum_node_cut(G)}')
