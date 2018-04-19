
# coding: utf-8

# In[2]:


import scipy.io
import matplotlib.pyplot as pyplot
import matplotlib.cm as cm


# In[8]:

def main(imagename):
    img=scipy.misc.imread(imagename)
    img=img/255.0
    image_new=[]

    for i in img:
        temp=[]
        for j in i:
            if j<0.4:
                temp.append(0.0)
            else:
                temp.append(1.0)
        image_new.append(temp)

    scipy.misc.imsave('super_contrast.jpg', image_new)

