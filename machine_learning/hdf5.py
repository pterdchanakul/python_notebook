# A module related to HDF file
import numpy as np
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import glob
import os.path
import h5py
import time

# Global Variable
module_path = os.path.dirname(__file__)

def input_image_data():

    # Read PNG data
    png_path = module_path + '/nih_sample_data/images/*.png'
    hdf5_path = module_path + '/nih_sample_data/'

    # Prepare data into hdf5
    img_rows, img_cols, img_ch = 1024, 1024, 1
    print(png_path)

    # read data into keras
    for filename in glob.glob(png_path):
        img = load_img(filename)


start_time = time.time()

input_image_data()

end_time = time.time()
print(end_time - start_time)
