def create_tour(nodes):
    eulerTour = []
    for idx,node in enumerate(nodes):
        if idx == len(nodes)-1:
            eulerTour.append((node,nodes[0]))
        else:
            eulerTour.append((node,nodes[idx+1]))
    return eulerTour

def find_eulerian_tour(graph):
    tour = []
    edge = graph[0]

    while graph != []:
    	tour.append(edge[0],edge[1])
    	#remove edge
    	graph.remove(edge)

    	#find next connectiong edge