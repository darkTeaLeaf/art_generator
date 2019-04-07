from chromosome import Chromosome
import random

pop_num = 3
population = []
color_num = 20
parents = []


def generate_init_pop(file_name):
    for i in range(1, pop_num + 1):
        chromosome = Chromosome(file_name)
        population.append(chromosome)


def fitness_function():
    for chromosome in population:
        chromosome.count_color_num()


def selection_function():
    parents.clear()
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
    for i in range(1, pop_num + 1):
        population.append(generate_child())


def generate_child():
    child = parents[1]
    for k in range(1, int(child.pix_num / 10) + 1):
        i = random.randint(0, len(child.image_array) - 1)
        j = random.randint(0, len(child.image_array[0]) - 1)
        child.image_array[i][j] = parents[0].image_array[i][j]

    return child


def mutation():
    for chromosome in population:
        new_chromosome = chromosome
        population.remove(chromosome)
        for k in range(1, int(chromosome.pix_num / 2) + 1):
            i = random.randint(0, len(chromosome.image_array) - 1)
            j = random.randint(0, len(chromosome.image_array[0]) - 1)
            change_color(chromosome, new_chromosome, i, j)
        population.append(new_chromosome)


def change_color(chromosome, new_chromosome, i, j):
    pix = chromosome.image_array[i][j]
    color = chromosome.image_array[i][j]
    min_difference = 10000000

    first_i_border = i - 1
    second_i_border = i + 1
    first_j_border = j - 1
    second_j_border = j + 1

    if i == 0:
        first_i_border = i
        second_i_border = i + 1
    if i == (len(chromosome.image_array[0]) - 1):
        first_i_border = i - 1
        second_i_border = i
    if j == 0:
        first_j_border = j
        second_j_border = j + 1
    if j == (len(chromosome.image_array) - 1):
        first_j_border = j - 1
        second_j_border = j

    for n in range(first_i_border, second_i_border):
        for m in range(first_j_border, second_j_border):
            if not (n == i and m == j):
                difference = 0
                difference += abs(chromosome.image_array[n][m][0] - pix[0])
                difference += abs(chromosome.image_array[n][m][1] - pix[1])
                difference += abs(chromosome.image_array[n][m][2] - pix[2])
                if min_difference > difference:
                    color = chromosome.image_array[n][m]
                    min_difference = difference

    new_chromosome.image_array[i][j] = color


def termination():
    fitness_function()

    chromosome = population[0]

    for ch in population:
        if abs(ch.fitness_score - color_num) < (chromosome.fitness_score - color_num):
            chromosome = ch

    return chromosome
