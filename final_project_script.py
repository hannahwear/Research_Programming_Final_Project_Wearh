# -*- coding: utf-8 -*-
"""
Research Programming Final Project
Hannah Wear
"""

from matplotlib import pyplot as plt
from skimage import io
from skimage.feature import blob_dog
from skimage.color import rgb2gray
import math
import numpy as np



def area_of_circle(r):
    area = r**2 * math.pi
    return area

def doit(filename):
    dat = io.imread(filename)
    dat = rgb2gray(dat)

    blobs = blob_dog(dat, max_sigma=12, threshold=.25)
    blobs[:, 2] = blobs[:, 2] * (2 ** 0.5)

    io.imshow(dat)
    for blob in blobs:
        y, x, r = blob
        c = plt.Circle((x, y), r, color='r', linewidth=2, fill=False)
        plt.gca().add_patch(c)
    plt.show()

    print (blobs[:,2].size)

    r = (blobs[:,2])
    print (r)
    print (area_of_circle(r))
    avg_r = np.mean(area_of_circle(r))
    print (avg_r)
    
    #Distance from average x 
    avg_x = np.mean(blobs[:,0])
    x = (blobs[:,0])
    avg_x_dist = (x-avg_x)
    print (avg_x_dist)
    
    #Distance from average y
    avg_y = np.mean(blobs[:,1])
    y = (blobs[:,1])
    avg_y_dist = (y-avg_y)
    print (avg_y_dist)
    
    return blobs # for potential further processing
    

images = (('Image of germ cell nests in ovary', 'germ_cell_nest.jpg'),
('Image of germ cell nest breakdown', 'germ_nest_breakdown.gif'),
('Image of mouse ovary at post-natal day 1.0', 'mouse_ovary_P1.png')) 
# list of (filename, description) 

for image in images:
    print('Processing: {}'.format(image[0]))
    doit(image[1])
