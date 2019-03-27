from PIL import Image
import numpy as np


class Chromosome:

    def __init__(self, file_name):
        img = Image.open(file_name)
        img.load()
        self.image_array = np.asarray(img, dtype="int32")
        self.fitness_score = 0

    def count_color_num(self):
        color_array = []
        for i in self.image_array:
            for j in i:
                append = True
                for k in color_array:
                    if k[0] == j[0] and k[1] == j[1] and k[2] == j[2]:
                        append = False
                if append:
                    color_array.append(j)
        self.fitness_score = len(color_array)
