import numpy as np
from matplotlib.pyplot import imread
from PIL import Image

class CustomImageClass:
    
    #  Converting image to a 2d array whewre  each row is of the form [r, g, b]. 
    #  A ~path~ to an image must be given
    def image_to_array(path_to_image):
        im_arr = imread(path_to_image)
        data = np.array(im_arr)
        return data

    #saves an image created from an array. Array image name must be provided. Extension will be added automatically.
    #Absolute path to a directory to save can be provided. If not than saves to home directory for the class
    def save_image(arr, name):
        im = Image.fromarray(arr)
        im.save(name + ".jpg")
        im.show()

    #Gets certain pixel with given coordinates x, y, c
    def get_pixel(im, x, y, c):
        shape = im.shape
        #Checking for valid values. If not then use clamp padding
        if (x < 0):
            x = 0
        elif (x >= shape[0]):
            x = shape[0] - 1
        if (y < 0):
            y = 0
        elif (y >= shape[1]):
            y = shape[1] - 1
        if (c < 0):
            c = 0
        elif (c > 2):
            c = 2
        return im[x, y, c]

    #Sets a pixel on given coordinates [x, y, c] to given value [value]
    def set_pixel(im, x, y, c, value):
        shape = im.shape
        #Checking for valid values. If not return nothing
        if ((x < 0) | (x >= shape[0]) | (y < 0) | (y >= shape[1]) | (c < 0) | (c > 2)):
            return "Pass proper image values!"
        im[x, y, c] = value
        return im

    def image_to_grayscale(im):
        new_im = np.zeros((im.shape[0], im.shape[1]))
        for row in range(im.shape[0]):
            for col in range (im.shape[1]):
                new_im[row, col] = int(get_pixel(im, row, col, 0) * 0.299 + get_pixel(im, row, col, 1) * 0.587 + get_pixel(im, row, col, 2) * 0.114)
        return new_im