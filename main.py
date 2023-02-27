import random

# Define parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
TARGET_STRING = "HELLO WORLD"

# Define helper functions
def random_string(length):
    return "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ") for _ in range(length))

def fitness(string):
    return sum(1 for a, b in zip(string, TARGET_STRING) if a == b)

def mutate(string):
    return "".join(
        c if random.random() > MUTATION_RATE else random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        for c in string
    )

# Create initial population
population = [random_string(len(TARGET_STRING)) for _ in range(POPULATION_SIZE)]

# Evolve population
generation = 1
while True:
    # Evaluate fitness of each string in the population
    fitnesses = [fitness(string) for string in population]
    
    # Check if we've found the target string
    if TARGET_STRING in population:
        print(f"Found target string '{TARGET_STRING}' after {generation} generations")
        break
    
    # Print current best string
    best_string = max(population, key=fitness)
    print(f"Generation {generation}: {best_string} (fitness = {fitness(best_string)})")
    
    # Select parents for next generation
    parents = random.choices(population, weights=fitnesses, k=2)
    
    # Create offspring by crossover and mutation
    offspring = []
    for i in range(POPULATION_SIZE):
        parent1, parent2 = random.choices(parents, k=2)
        offspring.append(mutate("".join(
            c1 if random.random() < 0.5 else c2
            for c1, c2 in zip(parent1, parent2)
        )))
    
    # Replace old population with new offspring
    population = offspring
    
    generation += 1
