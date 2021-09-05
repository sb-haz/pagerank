def pagerank(edges, a, iters):

    nodes = set()
    for edge in edges:
        nodes.add(edge[0])

    P = np.empty((0,len(nodes)), float)

    for node in nodes:
        connecting_edges = []
        for edge in edges:
            if (node == edge[0]):
                connecting_edges.append(edge[1])

        l = []
        for n in nodes:
            if n in connecting_edges:
                x = (1 - a) / len(connecting_edges)
                l.append(x)
            else:
                x = a / (len(nodes) - len(connecting_edges))
                l.append(x)

        P = np.append(P, np.array([l]), axis=0)

    x = np.array([[1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes)]])

    for _ in range(iters):
        x = x.dot(P)

    return x[0]

edges = {(0,2),(0,3),(0,5),(0,6),(0,7),(0,9),(1,4),(1,6),(2,4),(3,2),(4,2),(4,3),(4,9),(5,0),(5,1),(5,6),(5,8),(5,9),(6,4),(6,6),(7,2),(7,3),(7,4),(7,5),(7,6),(7,9),(8,2),(8,3),(8,5),(9,5)}
print("Page Rank -", pagerank(edges, 0, 100))