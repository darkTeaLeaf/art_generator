from PIL import Image
import numpy as np
from chromosome import Chromosome


# def load_image(file_name):
#     img = Image.open(file_name)
#     img.load()
#     data = np.asarray(img, dtype="int32")
#     return data
#
#
# def save_image(np_data, out_file_name):
#     img = Image.fromarray(np_data, "RGB")
#     img.save(out_file_name)


# print(load_image('C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\751px-VanGogh-starry_night.jpg'))

ch = Chromosome('C:\\Users\\Dell\\Desktop\\My disk\\Sketches\\9px_image.jpg')
print(ch.image_array)
ch.count_color_num()
print(ch.fitness_score)
print(ch.pix_num)
