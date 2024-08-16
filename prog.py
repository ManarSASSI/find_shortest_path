import csv
class Graph :
    def __init__(self,n=0):
        self.n=n
        self.index_vertice = {}
        self.vertice = {}
        self.edge= {}
        self.current_index = 0
    
    def add_vertice(self,s):
        if s not in self.vertice :
            self.n +=1
            self.index_vertice[s]= self.current_index
            self.vertice[s] = set()
            self.current_index +=1

    def add_edge(self, s, e, p):
        self.add_vertice(s)
        self.add_vertice(e)
        self.vertice[s].add(e)
        self.vertice[e].add(s)
        self.edge[(s, e)]=p
        self.edge[(e, s)]=p
        
    def exist_edge(self, e, s):
        if (s in self.vertice[e]) and (e in self.vertice[s]):
            return True
        return False
    
    def get_neighbours(self,s):
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
    distances[start]= 0
    Q = set(graph.get_vertices())
    while Q :
        global sommet 
        sommet = min(Q, key = lambda k: distances[k])
        #for s1 in Q:
            #if distances[graph.index_vertice[s1]] < mini:
               # mini = distances[graph.index_vertice[s1]]
               # sommet = graph.index_vertice[s1]
        Q.remove(sommet)

        if sommet == end or distances[sommet] == float('inf'):
            break
        
        for neighbours in graph.get_neighbours(sommet):
            if distances[neighbours] > distances[sommet] + graph.edge[(sommet,neighbours)]:
                distances[neighbours] = distances[sommet] + graph.edge[(sommet,neighbours)]
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

fichier = "C:\\Users\\MAISON INFO\\Documents\\Stage 2\\Classeur1.csv"
ma_graph = csv_to_graph(fichier)
    
start = 'tunis'
end =  'kebili'

chemin = dijkstra(ma_graph, start , end)
print("chemin:",chemin)
     
    
    
