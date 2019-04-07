import genetic_algorithm

image_name = 'C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\init7.jpg'
final_name = 'C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\final7.jpg'
iterations_num = 30

genetic_algorithm.generate_init_pop(image_name)

print('End of initial population\'s generation')

for i in range(1, iterations_num + 1):
    genetic_algorithm.fitness_function()

    genetic_algorithm.selection_function()

    genetic_algorithm.crossover()

    genetic_algorithm.mutation()

    print('End of ' + str(i) + ' iteration')

result = genetic_algorithm.termination()

print('End of termination')

result.save_image(final_name)
