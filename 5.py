import matplotlib.pyplot as plt
import cv2
import numpy as np
print("read images using opencv")
five = cv2.imread("D:/Studi Doctoral/Semester 2/Pengenalan Pola/Praktikum/Praktikum 2/5.png")
print(five.shape)
print(five.size)
cv2.imshow('test', five)
cv2.waitKey(0)

