#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
from matplotlib import pyplot as plt


# In[30]:


bg = cv2.imread('images/bg.jpeg', 1)
#bg


# In[21]:


fg = cv2.imread('images/text.png', 1)


# In[22]:


bg.shape


# In[23]:


fg.shape


# In[11]:


plt.imshow(bg)
plt.show()


# In[24]:


plt.imshow(fg)
plt.show()


# In[7]:


#Resizing the images as it will show an error if we try to blend images of different sizes


# In[17]:


dim = (700, 400)


# In[18]:


resized_bg = cv2.resize(bg, dim, interpolation = cv2.INTER_AREA)


# In[19]:


plt.imshow(resized_bg)
plt.show()


# In[25]:


resized_fg = cv2.resize(fg, dim, interpolation = cv2.INTER_AREA)


# In[26]:


plt.imshow(resized_fg)
plt.show()


# In[60]:


blend = cv2.addWeighted(resized_bg, 0.5, resized_fg, 0.8, 0.0)
#blend


# In[61]:


cv2.imwrite('blendedimage.png', blend)


# In[62]:


plt.imshow(blend)
plt.show()

