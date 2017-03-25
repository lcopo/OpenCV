#Importing libraries
import cv2
import numpy as np

#Load an image: cv2.imread()
#First argument: Name File
#Second argument:
        #cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
        #cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
        #cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
        #Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

#Load a color image in grayscale
img = cv2.imread('EiffelTower.jpg', 0)

#Display an image: cv2.imshow()
#First argument: String window name
#Second argument: Image
cv2.imshow('The Eiffel Tower', img)

#cv2.waitKey function to display the image for specified milliseconds.
#With 0 as argument, the image is displayed infinitely until keyboard event.
cv2.waitKey(0)

#cv2.destroyAllWindows() function destroys all the windows created.
cv2.destroyAllWindows()

#cv2.namedWindow in case we need to show an image which is bigger than the screen resolution
#By default, the flag is cv2.WINDOW_AUTOSIZE
#To resize the image, the following flag must be specified: cv2.WINDOW_NORMAL
cv2.namedWindow('The Eiffel Tower', cv2.WINDOW_NORMAL)
cv2.imshow('The Eiffel Tower', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Write an image: cv2.imwrite()
#First argument: File name
#Second argument: The image to save
cv2.imwrite('EiffelTowerGray.jpg', img)

#Using Matplotlib
from matplotlib import pyplot as plt

img = cv2.imread("EiffelTower.jpg", 0)

plt.imshow(img, cmap = 'gray', interpolation='bicubic')
plt.xticks([], plt.yticks([])) #To hide tick values on X and Y axis
plt.show()