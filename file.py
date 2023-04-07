import os
import cv2
friendFolderPath = "C:/Users/seane/Downloads/FriendImages"
images = []

for file in os.listdir(friendFolderPath):
    name, ext = os.splitext(file)
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = friendFolderPath + "/" + file
        print(file_name)
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
width, height, channels = frame.shape

size = (width, height)

out = cv2.VideoWriter("project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(0, count -1):
    cv2.imread()
    out.write()