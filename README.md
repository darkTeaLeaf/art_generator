# Art generator based on Genetic algorithm
Problem formulation: given several test input images of 512x512 pixels. It needs to produce via any evolutionary algorithm
another 512x512 from a single test image your computational artist. 

For the solution, there was decided to choose the Genetic algorithm which was implemented using Python library Pillow for work with images.

# The decision about what is art?
According to very unspecific problem description, we need to define what algorithm should provide, so it will be rated as a piece of art.
Actually, it special for every person. Thus, as for me I have decided to create algorithm which will generate pixel art 
(see real example of pixel art below) from any picture it will given. 
The two main points are using a few colors and placing them strictly pixel by pixel, therefore we will be given such a great picture.

![Example of pixel art](http://yumenohikari.ru/img/articles/45/pixel.jpg)

# Genetic algorithm implementation
Genetic algorithm goes through the following steps:
* initialization of the first population of chromosomes consisting of some amount of genes
* fitness function (evaluate each chromosome according to their suitability)
* selection function (choose the best chromosomes according to fitness score)
* crossover (merge two best chromosomes to produce new population)
* mutation (add some noise to new population)
* termination (finish iterations and choose the best chromosome from the last population)

## Initialization of the first population
For the current implementation, each population consists of 3 (number can be changed) images as chromosomes with pixels as genes.
The first population is generated from copies of picture which is given initially. 

## Fitness function
To determine that picture is pixelized enough we need to count how much it has different colours. </br>
At first, a number of colours which we want on the picture (can be assumed as a level of result image detailing, fewer colours lead to less detailing) is set. Then algorithm counts how much unique colours in each chromosome and this number becomes a fitness score for a chromosome.

## Selection function
In this part of the algorithm, we choose two chromosomes with fitness scores which are closest to the number of colours we want. 
Chosen ones will be the best in the population and become parents for the future population. 

## Crossover
At the moment we need to generate the whole new population which will have equal parts from parents selected on the previous step. 
For this purpose, the algorithm takes randomly a half of all pixels from one parent and the next half from the second, therefore 
the necessary amount of different chromosomes for the new population is generated.

## Mutation
To achieve the main purpose of the algorithm we need to change colours of pixels somehow. A decreasing number of unique colours on a picture can be reached by changing the colour of pixel to colour of another pixel which is close to the first one. 
The algorithm uses this strategy: goes through eight pixels which border to initial, determines the pixel with closest colour and changes colour initial to it. The process is applied to random pixels of each chromosome in population.  

# Testing on different inputs
The first on was the picture (200x125) of "The Birth of Venus" by Sandro Botticelli. And you can see result after 5 iterations with color number 50, 3 chromosomes in population.

![Initial picture](https://i.ibb.co/V2ZwD9p/init.jpg)
![Result picture](https://i.ibb.co/SyPtpWh/final.jpg)

According to initial task, we need to test algorithm on image 512x512. So, here it is the picture of cute cats :3 </br>
Using 6 iterations, color number 50, 3 chromosomes in population we got the following result (see picture below).

![Initial picture](https://i.ibb.co/F3fC1tv/init4.jpg)

