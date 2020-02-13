#!/usr/bin/env python3
from PIL import Image, ImageDraw
import cv2
import numpy as np
import os

# home_path = "os.getcwd() + "/picture""
home_path=""

class ColorMode:
    def __init__(self, filename):
        self.filename = filename[:filename.find('.')]
        self.image = Image.open(filename).convert('RGB')
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()

    def sepia(self,depth=30):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if (a > 255):
                    a = 255
                if (b > 250):
                    b = 255
                if (c > 255):
                    c = 255
                self.draw.point((i, j), (a, b, c))
        self.image.save(home_path+self.filename + '_sepia.jpg', format='jpeg')
        del self.draw
        return home_path+self.filename + '_sepia.jpg'
    def negative(self):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                self.draw.point((i, j), (255-a, 255- b, 255-c))
        self.image.save(home_path+self.filename + '_negative.jpg', format='jpeg')
        # output.seek(0)
        del self.draw
        return home_path+self.filename + '_negative.jpg'
    def black_white(self, factor=50):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c)

                if (S > (((255 + factor) // 2)  * 3)):
                    a, b, c = 0, 0, 0
                else :
                    a, b, c = 255, 255, 255
                self.draw.point((i, j), (a, b, c))
        self.image.save(home_path+self.filename + '_black_white.jpg', format='jpeg')
        del self.draw
        return home_path+self.filename + '_black_white.jpg'
    def white_black(self, factor=50):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c)

                if (S > (((255 + factor) // 2)  * 3)):
                    a, b, c = 255, 255, 255
                else :
                    a, b, c = 0, 0, 0
                self.draw.point((i, j), (a, b, c))
        self.image.save(home_path+self.filename + '_white_black.jpg', format='jpeg')
        del self.draw
        return home_path+self.filename + '_white_black.jpg'
    def gray(self):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = (a + b + c) // 3
                self.draw.point((i, j), (S, S, S))
        self.image.save(home_path+self.filename + '_gray.jpg', format='jpeg')
        del self.draw
        return home_path+self.filename + '_gray.jpg'



# class CV2:
#     def __init__(self, image):
#         self.src = image
#         self.image = Image.open(image).convert("RGB")
#
#     # def deep_find_face(self):
#     #     opencv_image = (np.array(self.image))[:, :, ::-1].copy()
#     #     opencv_gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
#     #     faces = face_cascade.detectMultiScale(opencv_gray, minNeighbors=15, minSize = (10, 10))
#     #     faces_detected = format(len(faces))
#     #     if faces_detected == 0:
#     #         return self.src, "Faces not find"
#     #     else :
#     #         mark = ImageDraw.Draw(self.image)
#     #         # for (x, y, w, h) in faces:
#     #         mark.rectangle([(x, y), (x+w, y+h)], (0, 255, 255))
#     #         roi_gray = opencv_gray[y:y+h, x:x+w]
#     #         roi_color = opencv_image[y:y+h, x:x+w]
#     #             # eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#     #             # for (ex, ey, ew, eh) in eyes:
#     #             #     mark.rectangle([ex, ey, x+w, y+h], (255, 255, 255))
#     #
#     #         # self.image.save(self.src + '_find_face.jpg', formag="jpeg")
#     #         self.image.show(faces_detected)
#     #         # return self.src+'_find_face.jpg', faces_detected

face_cascade = cv2.CascadeClassifier('./deep/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./deep/haarcascade_eye.xml')

def deep_find_face(image):
    CVimage = cv2.imread(image)
    gray = cv2.cvtColor(CVimage, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, minNeighbors=15, minSize = (10, 10))
    faces_detected = format(len(faces))
    if faces_detected == 0:
        return image, "A Face don't find"
    else :
        for (x, y, w, h) in faces:
            cv2.rectangle(CVimage, (x, y), (x+w, y+h), (0, 255, 255), 10)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = CVimage[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 255), 2)
        cv2.imwrite(image + '_find_face.jpg', CVimage)
        return image+'_find_face.jpg', faces_detected

# #
# class FindPeople:
#     def __init__(self)
