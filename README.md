# Art generator based Genetic algorithm
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

## Initialization of the first population
For the current implementation, each population consists of 3 (number can be changed) images as chromosomes with pixels as genes.
The first population is generated from copies of picture which is given initially. 

## Fitness function
To determine that picture is pixelized enoungh we need to count how much it has different colors. </br>
At fisrt, number of colors whcih we want on picture (can be assumed as a level of result image detalization, 
less colors lead to less detalization) is set. Then algorithm counts how much unique colors in each chromosome and this number becomes 
a fitness score for a chromosome.

## Selection function
In this part of algorithm, we choose two chromosomes with fitness scores which are closest to number of color we want. 
Choosed ones will be the best in the population and become parents for the future population. 

## Crossover
At the moment we need to generate the whole new population which will have equal parts from parents selectes on the previous step. 
For this purpose algorithm takes randomly a half of all pixels from one parent and the next half from the second, therefore 
necessary amount of different chromosomes in the new population is generated.
