import networkx as nx
import random

# Sample graph representing the wireless ad hoc network
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])

# Define parameters
population_size = 10
generations = 100
mutation_rate = 0.1


# Generate initial population
def generate_individual():
    return random.sample(list(G.nodes()), len(G.nodes()))


population = [generate_individual() for _ in range(population_size)]


# Fitness function (simple, for demonstration purposes)
def fitness(individual):
    # Calculate fitness based on the length of the route
    return nx.shortest_path_length(G, source=individual[0], target=individual[-1])


# Genetic Algorithm
for generation in range(generations):
    # Evaluate fitness of each individual
    fitness_scores = [fitness(individual) for individual in population]

    # Select parents based on fitness scores (tournament selection)
    parents = random.choices(population, weights=fitness_scores, k=2)

    # Perform crossover (simple one-point crossover)
    crossover_point = random.randint(1, len(G.nodes()) - 1)
    child = parents[0][:crossover_point] + parents[1][crossover_point:]

    # Perform mutation
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, len(G.nodes()) - 1)
        new_node = random.choice(list(G.nodes()))
        child[mutation_point] = new_node

    # Replace worst individual with the child
    worst_index = min(range(len(population)), key=lambda i: fitness_scores[i])
    population[worst_index] = child

# Select the best individual as the route
best_route = min(population, key=fitness)
print("Best route:", best_route)
print("Fitness:", fitness(best_route))
