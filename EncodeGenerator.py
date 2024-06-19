import cv2
import os

# importing student images

folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
for path in pathList:
    imgPath = os.path.join(folderPath, path)
    imgList.append(cv2.imread(imgPath))

print(len(imgList))
