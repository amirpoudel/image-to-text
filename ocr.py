import pytesseract
from PIL import Image
import cv2
import os
import csv

# Set the path to Tesseract executable (you may need to adjust this based on your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image using OpenCV
image = cv2.imread('screenshot.png')

# Convert the image to grayscale (required for Tesseract)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to perform OCR and extract text
text = pytesseract.image_to_string(gray_image)

# write to data/data.txt the extracted text

with open('data/data.txt', 'w') as file:
    file.write(text)

with open('data/index.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["file","source"])
    writer.writerow(["data.txt","https://d3fend.mitre.org/"])

# Print a confirmation message
print("Text extracted from the image has been written to data.txt.")