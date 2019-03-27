from chromosome import Chromosome
import random

pop_num = 5
population = []
color_num = 20
parents = []


def generate_init_pop(file_name):
    for i in range(1, pop_num):
        chromosome = Chromosome(file_name)
        population.append(chromosome)


def fitness_function():
    for chromosome in population:
        chromosome.count_color_num()


def selection_function():
    first_fit = population[0]
    second_fit = population[1]
    for chromosome in population:
        if abs(chromosome.fitness_score - color_num) < abs(first_fit.fitness_score - color_num):
            first_fit = chromosome
        elif abs(chromosome.fitness_score - color_num) < abs(second_fit.fitness_score - color_num):
            second_fit = chromosome
    parents.append(first_fit)
    parents.append(second_fit)


def crossover():
    population.clear()
    for i in range(1, pop_num):
        population.append(generate_child())


def generate_child():
    child = parents[1]
    for k in range(1, child.pix_num / 2):
        i = random.randint(0, child.pix_num - 1)
        j = random.randint(0, child.pix_num - 1)
        child[i][j] = parents[0][i][j]

    return child


def mutation():
    for chromosome in population:
        for k in range(1, chromosome.pix_num / 2):
            i = random.randint(0, chromosome.pix_num - 1)
            j = random.randint(0, chromosome.pix_num - 1)
            change_color(chromosome, i, j)


def change_color(chromosome, i, j):
    # TODO
    return
