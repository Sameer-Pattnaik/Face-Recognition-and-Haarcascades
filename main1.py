from pyzbar.pyzbar 
import decode from Pil 
import Image from cv2,time 
import csv

video=cv2.VideoCapture(0)

students=[]

with open("1.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        students.apppend((row[1]))