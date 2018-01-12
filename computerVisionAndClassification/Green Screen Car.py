
# coding: utf-8

# # Color Masking, Green Screen

# ### Import resources

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np
import cv2

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Read in and display the image

# In[2]:


# Read in the image
image = mpimg.imread('images/car_green_screen.jpg')

# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)

# Display the image
plt.imshow(image)


# ### Define the color threshold

# In[3]:


# Define our color selection boundaries in RGB values
lower_green = np.array([0,180,0]) 
upper_green = np.array([100,255,100])


# ### Create a mask

# In[4]:


# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)

# Vizualize the mask
plt.imshow(mask, cmap='gray')


# In[5]:


# Mask the image to let the car show through
masked_image = np.copy(image)

masked_image[mask != 0] = [0, 0, 0]

# Display it!
plt.imshow(masked_image)


# ## TODO: Mask and add a background image

# In[6]:


# Load in a background image, and convert it to RGB 
background_image = mpimg.imread('images/sky.jpg')

print(background_image.shape)


## TODO: Crop it or resize the background to be the right size (450x660)
row_crop = 62
col_crop = 182

bg_cropped = background_image[row_crop:-row_crop, col_crop:-col_crop, :]
bg_cropped = cv2.resize(bg_cropped, (660, 450))

print(bg_cropped.shape)

## TODO: Mask the cropped background so that the pizza area is blocked

# Mask the image to let the car show through
masked_image2 = np.copy(bg_cropped)

masked_image2[mask != 255] = [0, 0, 0]


# Hint mask the opposite area of the previous image

## TODO: Display the background and make sure 
# Display it!
plt.imshow(masked_image2)


# ### TODO:  Create a complete image

# In[10]:


## TODO: Add the two images together to create a complete image!
# complete_image = masked_image + crop_background

new_image = masked_image + masked_image2

plt.imshow(new_image)

