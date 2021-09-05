def pagerank(edges, a, iters):

    # Set including all possible starting nodes
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])

    # Empty array
    P = np.empty((0,len(nodes)), float)

    # Iterate through every node
    # Calculate row of probabilities (to jump from current node)
    for node in nodes:
        connecting_edges = []
        for edge in edges:
            # Find all nodes in given edges set
            if (node == edge[0]):
                # Add (the connecting edges) to a list
                connecting_edges.append(edge[1])

        l = []
        # Iterate through nodes again, to build row of jump probabilities (in list l)
        for n in nodes:
            # Connecting nodes have probability of '1 -  a'
            # If 'a' was 10%, they'll have 90% probability combined
            if n in connecting_edges:
                x = (1 - a) / len(connecting_edges)
                l.append(x)
            # Non-connecting nodes have probability of 'a' to add random teleportation
            # Both connecting and non-connecting together will have a probability of 1
            else:
                x = a / (len(nodes) - len(connecting_edges))
                l.append(x)

        # Add list 'l' to transition probability matrix as new row
        P = np.append(P, np.array([l]), axis=0)

    # Probability vector (1/n)
    x = np.array([[1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes), 1/len(nodes)]])

    # Iterate 'iters' times to find steady state, x * P^iters
    for _ in range(iters):
        x = x.dot(P)

    # Return resulting vector
    return x[0]

# Webpage edges
edges = {(0,2),(0,3),(0,5),(0,6),(0,7),(0,9),(1,4),(1,6),(2,4),(3,2),(4,2),(4,3),(4,9),(5,0),(5,1),(5,6),(5,8),(5,9),(6,4),(6,6),(7,2),(7,3),(7,4),(7,5),(7,6),(7,9),(8,2),(8,3),(8,5),(9,5)}
# Function call
print("Page Rank -", pagerank(edges, 0, 100))