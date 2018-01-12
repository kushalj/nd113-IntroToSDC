
# coding: utf-8

# # HSV colorspace

# ### Import resources

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read in RGB image

# In[2]:


# Read in the image
image = mpimg.imread('images/car_green_screen2.jpg')

plt.imshow(image)


# ### RGB threshold 
# 
# Visualize the green threshold you defined in the previous, consistent green color case.

# In[3]:


# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])

# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)


# ### Convert to HSV

# In[4]:


# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# HSV channels
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# Visualize the individual color channels
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20,10))
ax1.set_title('H channel')
ax1.imshow(h, cmap='gray')
ax2.set_title('S channel')
ax2.imshow(s, cmap='gray')
ax3.set_title('V channel')
ax3.imshow(v, cmap='gray')


# ### TODO: Mask the green area using HSV color space

# In[19]:


## TODO: Define the color selection boundaries in HSV values
# Define our color selection boundaries in RGB values
lower_green = 0
upper_green = 130


## TODO: Define the masked area and mask the image
# Don't forget to make a copy of the original image to manipulate
image2 = np.copy(image)

# Define the masked area
mask = cv2.inRange(image2[:,:,0], lower_green, upper_green)

# Mask the image to let the car show through
masked_image = np.copy(image2)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)

