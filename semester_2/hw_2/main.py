import networkx as nx
import matplotlib.pyplot as plt


# создадим полный граф с четырьмя вершинами
G = nx.complete_graph(4)

# отобразим граф без параметров
nx.draw(G)
plt.axis('equal')
plt.show()

# выведем количество вершин и ребер
print(f'Количество вершин: {G.number_of_nodes()}')  # 4
print(f'Количество ребер: {G.number_of_edges()}')  # 6

# выведем степень вершины 1 и смежные с ней вершины
print(f'Степень вершины 1: {G.degree[1]}')  # 3
print(f'Смежные вершины с вершиной 1: {list(G.neighbors(1))}')  # [0, 2, 3]

# удалим вершину 1 и снова выведем количество вершин и ребер
G.remove_node(1)
print(f'Количество вершин: {G.number_of_nodes()}')  # 3
print(f'Количество ребер: {G.number_of_edges()}')  # 3

# отобразим получившийся граф с размером узлов 1000 и их нумерацией
nx.draw(G, with_labels=True, node_size=1000)
plt.axis('equal')
plt.show()

# выведем степень вершины 2 и смежные с ней вершины
print(f'Степень вершины 2: {G.degree[2]}')  # 2
print(f'Смежные вершины с вершиной 2: {list(G.neighbors(2))}')  # [0, 3]
