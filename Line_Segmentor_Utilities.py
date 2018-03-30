
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


def is_background(rowno):
    row,col=mat.shape
    for i in range(0,col):
        if mat[rowno][i]<0.9:
            return False
    return True


# In[6]:


def get_matrix(row_no):
    matrix=[]
    row,col=mat.shape
    for i in range(row_no,row):
        if is_background(i)==False:
            z=mat[:,i]
            matrix.append(z)
        else:
            break
    matrix=np.matrix(matrix)
    matrix=np.transpose(matrix)
    pyplot.imshow(matrix,cmap=cm.gray)
    pyplot.show()
    image_arr.append(matrix.tolist())
    return i


# In[7]:


def get_line_img():
    row,col=mat.shape
    row_no=0
    new_img=[]
    for i in range(row):
        if is_background(i)==False:
            new_img.append(mat[i])
        else:
            if len(new_img)!=0:
                image_arr.append(new_img)
                new_img=[]
            


# In[3]:


def process_image():
    img=scipy.misc.imread('conv.png')
    img=img[:,:,0]
    img=img/255.0
    pyplot.imshow(img,cmap=cm.gray)
    pyplot.show()
    return img


# In[12]:


img=process_image()
image_arr=[]
mat=img
get_line_img()
for i in image_arr:
    pyplot.imshow(np.matrix(i),cmap=cm.gray)
    pyplot.show()

