def randomwalk(edges, a, iters):

    # Histogram to return
    histogram = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Set including all possible starting nodes
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])

    # Start at random node
    current_node = random.sample(nodes, 1)[0]

    # Iterate
    for _ in range(iters):

        # Potential nodes list, will randomly pick from list later, to go to next node
        potential_nodes = []

        # Search through all edges to find nodes connecting to starting node
        for edge in edges:
            if (current_node == edge[0]):

                # Add to potential nodes collection
                potential_nodes.append(edge[1])

        # Probability to not randomly teleport
        if random.random() > a:

            # Pick a random node to visit next from current node
            current_node = random.choice(potential_nodes)
            
        # Else teleport to random page
        else:
            # Pick a random node
            current_node = random.sample(nodes, 1)[0]

        # Add visited node to histogram
        histogram[current_node] = histogram[current_node] + 1

    # Loop through histogram values to normalise values from 0 to 1
    total = (sum(histogram))
    for index, value in enumerate(histogram):
        histogram[index] = round(value/total, 6)

    # Return results
    return histogram

# Webpages edges
edges = {(0,2),(0,3),(0,5),(0,6),(0,7),(0,9),(1,4),(1,6),(2,4),(3,2),(4,2),(4,3),(4,9),(5,0),(5,1),(5,6),(5,8),(5,9),(6,4),(6,6),(7,2),(7,3),(7,4),(7,5),(7,6),(7,9),(8,2),(8,3),(8,5),(9,5)}
# Function call
print("Random Walk -", randomwalk(edges, 0, 1000))