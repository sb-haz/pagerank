def randomwalk(edges, a, iters):

    histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    nodes = set()
    for edge in edges:
        nodes.add(edge[0])

    current_node = random.sample(nodes, 1)[0]

    for _ in range(iters):
        potential_nodes = []

        for edge in edges:
            if (current_node == edge[0]):
                potential_nodes.append(edge[1])

        if random.random() > a:
            current_node = random.choice(potential_nodes)
        else:
            current_node = random.sample(nodes, 1)[0]

        histogram[current_node] = histogram[current_node] + 1

    total = (sum(histogram))
    for index, value in enumerate(histogram):
        histogram[index] = round(value/total, 6)

    return histogram

edges = {(0,2),(0,3),(0,5),(0,6),(0,7),(0,9),(1,4),(1,6),(2,4),(3,2),(4,2),(4,3),(4,9),(5,0),(5,1),(5,6),(5,8),(5,9),(6,4),(6,6),(7,2),(7,3),(7,4),(7,5),(7,6),(7,9),(8,2),(8,3),(8,5),(9,5)}
print("Random Walk -", randomwalk(edges, 0, 1000))