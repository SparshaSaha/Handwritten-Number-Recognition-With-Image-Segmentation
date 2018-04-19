
# coding: utf-8

# In[4]:


import scipy.io
import numpy as np
import matplotlib.pyplot as pyplot
from PIL import Image
import matplotlib.cm as cm
from pprint import pprint
import scipy.misc
import PIL


# In[5]:
image_arr=[]

def is_background(rowno,mat):
    row,col=mat.shape
    for i in range(0,col):
        if mat[rowno][i]<0.9:
            return False
    return True


# In[7]:


def get_line_img(mat):
    row,col=mat.shape
    row_no=0
    new_img=[]
    for i in range(row):
        if is_background(i,mat)==False:
            new_img.append(mat[i])
        else:
            if len(new_img)!=0:
                image_arr.append(new_img)
                new_img=[]
            


# In[3]:


def process_image(ima):
    img=scipy.misc.imread(ima)
    #img=img[:,:,0]
    img=img/255.0
    return img


# In[12]:

def main(image_name):
    img=process_image(image_name)
    mat=img
    get_line_img(mat)
    return image_arr

