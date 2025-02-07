# konversi image
import cv2
ipb = cv2.imread("d:/Studi Doctoral/Semester 2/Pengenalan Pola/Praktikum/Praktikum 2/ipb.png")
ipb_gray = cv2.cvtColor(ipb, cv2.COLOR_BGR2GRAY)
cv2.imshow('logo',ipb_gray)
cv2.waitKey(0)
