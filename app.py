import csv
import tkinter as tk
from tkintermapview import TkinterMapView


class Graph:
    def __init__(self, n=0):
        self.n = n
        self.index_vertice = {}
        self.vertice = {}
        self.edge = {}
        self.current_index = 0

    def add_vertice(self, s):
        if s not in self.vertice:
            self.n += 1
            self.index_vertice[s] = self.current_index
            self.vertice[s] = set()
            self.current_index += 1

    def add_edge(self, s, e, p):
        self.add_vertice(s)
        self.add_vertice(e)
        self.vertice[s].add(e)
        self.vertice[e].add(s)
        self.edge[(s, e)] = p
        self.edge[(e, s)] = p

    def exist_edge(self, e, s):
        if (s in self.vertice[e]) and (e in self.vertice[s]):
            return True
        return False

    def get_neighbours(self, s):
        return self.vertice[s]

    def get_vertices(self):
        return list(self.vertice.keys())


def csv_to_graph(fichier):
    graph = Graph()
    with open(fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            pays1, pays2, distances = row['pays1'].strip(), row['pays2'].strip(), int(row['distances'])
            graph.add_edge(pays1, pays2, distances)
        return graph


def dijkstra(graph, start, end):
    predecesseur = {}
    distances = {v: float('inf') for v in graph.get_vertices()}
    distances[start] = 0
    Q = set(graph.get_vertices())
    while Q:
        global sommet
        sommet = min(Q, key=lambda k: distances[k])
        Q.remove(sommet)

        if sommet == end or distances[sommet] == float('inf'):
            break

        for neighbours in graph.get_neighbours(sommet):
            if distances[neighbours] > distances[sommet] + graph.edge[(sommet, neighbours)]:
                distances[neighbours] = distances[sommet] + graph.edge[(sommet, neighbours)]
                predecesseur[neighbours] = sommet

    chemin_actuelle = []
    position = end

    while position in predecesseur:
        chemin_actuelle.append(position)
        position = predecesseur.get(position)

    if position != start:
        return []

    chemin_actuelle.append(start)

    chemin_actuelle.reverse()

    return chemin_actuelle


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Shortest Path ')
        self.geometry('800x600')
        self.resizable(False, False)
        self.iconbitmap("C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\logo.ico")

        #Container for map and input frame
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # MapView
        self.gmap_widget = TkinterMapView(container, width=800, height=400)
        self.gmap_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.gmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=50)
        self.gmap_widget.set_zoom(5)

        # adress marker
        self.gmap_widget.set_address("tunisia", marker=False)
        self.gmap_widget.set_zoom(15)

        #Input Frame
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.TOP, padx=10, pady=20, fill='x')

        self.label_start = tk.Label(input_frame, text="Start :")
        self.label_start.pack(side='left', padx=3, pady=5)

        self.entry_start = tk.Entry(input_frame)
        self.entry_start.pack(side='left', padx=3, pady=5, fill='x', expand=False)

        self.label_end = tk.Label(input_frame, text="End :")
        self.label_end.pack(side='left', padx=3, pady=5)

        self.entry_end = tk.Entry(input_frame)
        self.entry_end.pack(side='left', padx=5, pady=5, fill='x', expand=False)

        self.button = tk.Button(input_frame, text="Find", command=self.find_path)
        self.button.pack(side='left', padx=5, pady=5)

        self.result = tk.Label(input_frame, text="")
        self.result.pack(side='left', padx=5, pady=5, fill='x', expand=True)

    def find_path(self):
        start = self.entry_start.get().strip()
        end = self.entry_end.get().strip()

        file = "C:\\Users\\MAISON INFO\\Documents\\Stage 2\\projet\\Classeur1.csv"
        graph = csv_to_graph(file)

        if start not in graph.get_vertices() or end not in graph.get_vertices():
            self.result.config(text="start or end not in graph")
            return

        paths = dijkstra(graph, start, end)
        if not paths:
            self.result.config(text="No path found")
        else:
            self.result.config(text=f"shortest path  :{' -> '.join(paths)}")
            self.display_path_on_map(paths)

    def display_path_on_map(self, paths):
        self.gmap_widget.delete_all_marker()
        self.gmap_widget.delete_all_path()
        coordinates = []
        for location in paths:
            marker = self.gmap_widget.set_address(location, marker=True)
            if marker:
                coordinates.append(marker.position)
        if len(coordinates) > 1:
            self.gmap_widget.set_path(coordinates)


if __name__ == '__main__':
    app = App()
    app.mainloop()
