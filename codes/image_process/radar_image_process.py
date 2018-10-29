import cv2
import linecache
import numpy as np
from PIL import Image


filename = "RD_Ampl.txt"

data = []
with open(filename, 'r') as f:
	lines = f.readlines()
	for line in lines:
		oneLine = line.split()
		data.append([float(x) for x in oneLine])

maxv = max(max(data))
narray = np.array(data)
narray = narray/maxv*255.0
img = cv2.merge([narray.astype(np.uint8)])
#img = cv2.merge([narray])
cv2.imshow('test', img)
   
kernel = np.ones((3,3), np.uint8)
img_dilation = cv2.dilate(img, kernel, iterations = 2)
img_erosion = cv2.erode(img_dilation, kernel, iterations = 2)
cv2.imshow("dilation", img_dilation)
cv2.imshow("erosion", img_erosion)
#img_dilation1 = cv2.dilate(img_erosion, kernel, iterations = 1)
#img_erosion1 = cv2.erode(img_dilation1, kernel, iterations = 1)
#cv2.imshow("dilation1", img_dilation1)
#cv2.imshow("erosion1", img_erosion1)
img2 = cv2.GaussianBlur(img_erosion, (5,5), 3.0)
img2 = cv2.GaussianBlur(img2, (5,5), 3.0)
img_dilation1 = cv2.dilate(img2, kernel, iterations = 1)
img_erosion1 = cv2.erode(img_dilation1, kernel, iterations = 1)
img2 = cv2.GaussianBlur(img_erosion1, (5,5), 3.0)
cv2.imshow('gaussian', img2)
edge = cv2.Canny(img2, 50, 120)
cv2.imshow("canny", edge)
cv2.waitKey(0)
'''
hist = cv2.calcHist([img], [0], None, [256], [0.0, 255.0])
minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(hist) 
histImg = np.zeros([256,256,3], np.uint8) 
hpt = int(0.9* 256);  
for h in range(256):  
	intensity = int(hist[h]*hpt/maxVal)  
	cv2.line(histImg,(h,256), (h,256-intensity), [0,255,0]) 
cv2.imshow('histImg', histImg)	
cv2.waitKey(0)
'''

 
#narray = narray*255.0/maxv
#img = Image.fromarray(narray.astype(np.uint8))
#img.save('radar.bmp')