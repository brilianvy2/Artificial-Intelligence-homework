import random

# Define the graph
graph = {
    "A": [("B", 12), ("C", 4), ("D", 999), ("E", 999), ("F", 999), ("G", 12)],
    "B": [("A", 12), ("C", 8), ("D", 12), ("E", 999), ("F", 999), ("G", 999),],
    "C": [("A", 10), ("B", 8), ("D", 11), ("E", 3), ("F", 999), ("G", 9)],
    "D": [("A", 999), ("B", 12), ("C", 11), ("E", 11), ("F", 10), ("D", 999)],
    "E": [("A", 999), ("B", 999), ("C", 3), ("D", 11), ("G", 7), ("F", 6)],
    "F": [("A", 999), ("B", 999), ("C", 999), ("D", 10), ("E", 6), ("G", 9)],
    "G": [("A", 12), ("B", 999), ("C", 9), ("D", 999), ("E", 7), ("F", 9)]
}

# Define parameters
population_size = 50
generations = 100
initial_mutation_rate = 0.2

def create_individual():
    cities = list(graph.keys())
    cities.remove("A")
    random.shuffle(cities)
    return ['A'] + cities

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        for neighbor, distance in graph[current_city]:
            if neighbor == next_city:
                total_distance += distance
                break

    last_city = route[-1]
    for neighbor, distance in graph[last_city]:
        if neighbor == route[0]:
            total_distance += distance
            break

    return total_distance

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

population = set()
for _ in range(population_size):
    while True:
        individual = tuple(create_individual())
        if individual not in population:
            population.add(individual)
            break

best_route = None
best_distance = float('inf')
mutation_rate = initial_mutation_rate

for generation in range(generations):
    new_population = set()

    for _ in range(population_size):
        parent1, parent2 = random.sample(population, 2)
        child1, child2 = crossover(list(parent1), list(parent2))
        child1 = mutate(list(child1), mutation_rate)
        child2 = mutate(list(child2), mutation_rate)
        new_population.add(tuple(child1))
        new_population.add(tuple(child2))

    population = new_population
    current_best_route = min(population, key=lambda x: calculate_distance(list(x)))
    current_best_distance = calculate_distance(list(current_best_route))

    if current_best_distance < best_distance:
        best_route = current_best_route
        best_distance = current_best_distance

    mutation_rate *= 0.95

if best_route:
    best_distance = calculate_distance(list(best_route))
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
else:
    print("No valid routes found in the population.")