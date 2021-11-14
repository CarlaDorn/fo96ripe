import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
    
    im = Image.fromarray(X)
    im = im.resize(resize)
    return im
   
"""
You should create a way to resize an image from an array X.
The use of widgets is optional but you can take a look to interact.
We should be able to install this package in Google Colab from your Git
repo.
"""

#mytest
#imshow(np.array(Image.open('lena.png')), (100, 10)).show()

pass