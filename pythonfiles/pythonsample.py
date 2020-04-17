import cv2  
import numpy as np  
img = cv2.imread('dogimage.jpg')  
# ls = []  
# for i in range(255):  
# ls.append([i,i,i])  
# img = np.array([ls,ls,ls])  
#print(img.shape)  
#print(img)  
blue = img.copy()  
blue[:,:,1] = 0  
blue[:,:,2] = 0  
green = img.copy()  
green[:,:,0] = 0  
green[:,:,2] = 0  
red = img.copy()  
red[:,:,0] = 0  
red[:,:,1] = 0  
'''cv2.imwrite('TestBlue.JPG',blue)  
cv2.imwrite('TestGreen.JPG',green)  
cv2.imwrite('TestRed.JPG',red)'''  
cv2.imwrite('DogBlue.jpg',blue)  
cv2.imwrite('DogGreen.jpg',green)  
cv2.imwrite('DogRed.jpg',red)  
#cv2.imwrite('testimg.jpg',img)  