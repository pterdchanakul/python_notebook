# A module related to HDF file
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import glob
import os.path
import h5py
import time

# Global Variable
module_path = os.path.dirname(__file__)
png_path = module_path + '/data/nih_sample/images/*.png'
hdf5_path = module_path + '/data/nih_sample/data.hdf5'
img_rows, img_cols, img_ch = 1024, 1024, 1


def input_image_data():

    x_ray_inputs = [np.random.random((img_rows, img_cols, img_ch)) for i in range(len(glob.glob(png_path)))]
    # read data into keras
    for index, filename in enumerate(glob.glob(png_path)):
        x_ray_png = load_img(filename, color_mode='grayscale')
        x_ray_array = img_to_array(x_ray_png)
        # x_ray_inputs[index] = x_ray_array
        break

    print(x_ray_inputs.shape)

start_time = time.time()

input_image_data()

end_time = time.time()
print(end_time - start_time)
