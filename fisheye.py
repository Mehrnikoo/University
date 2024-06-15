import networkx as nx


def fisheye(graph, source_node, max_distance):
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph.nodes()}

    # Distance to source node is 0
    distances[source_node] = 0

    # Initialize a queue with source node
    queue = [source_node]

    # Perform BFS traversal
    while queue:
        current_node = queue.pop(0)
        current_distance = distances[current_node]

        # Iterate over neighbors of the current node
        for neighbor in graph.neighbors(current_node):
            # Update distance if it's smaller than the current distance
            new_distance = current_distance + 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                queue.append(neighbor)

                # Limit propagation based on max_distance
                if new_distance <= max_distance:
                    queue.append(neighbor)

    return distances


# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])

    # Call fisheye algorithm with source node 0 and max distance 2
    distances = fisheye(G, 0, 2)

    # Print distances from source node
    print("Distances from source node 0:")
    for node, distance in distances.items():
        print("Node:", node, "Distance:", distance)
