from chromosome import Chromosome

pop_num = 5
population = []
color_num = 20
parents = []


def generate_init_pop(file_name):
    for i in range(1, pop_num):
        chromosome = Chromosome(file_name)
        population.append(chromosome)


def fitness_function():
    for i in population:
        i.count_color_num()


def selection_function():
    first_fit = population[0]
    second_fit = population[1]
    for i in population:
        if abs(i.fitness_score - color_num) < abs(first_fit.fitness_score - color_num):
            first_fit = i
        elif abs(i.fitness_score - color_num) < abs(second_fit.fitness_score - color_num):
            second_fit = i
    parents.append(first_fit)
    parents.append(second_fit)
