import genetic_algorithm

image_name = 'C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\init2.jpg'
final_name = 'C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\final2.jpg'
iterations_num = 3

genetic_algorithm.generate_init_pop(image_name)

for i in range(1, iterations_num + 1):
    genetic_algorithm.fitness_function()

    genetic_algorithm.selection_function()

    genetic_algorithm.crossover()

    genetic_algorithm.mutation()

    print('End of ' + str(i) + ' iteration')

result = genetic_algorithm.termination()
# result = Chromosome(image_name)
result.save_image(final_name)
