import cv2
import numpy as np
import pytesseract
import sys
import pygame
import time


sys.stdout.reconfigure(encoding='utf-8')

# Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


pygame.mixer.init()

def play_sound(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the sound 
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing sound: {e}")

def ocr_image(image_path):
    # Read the image from the file path
    img = cv2.imread(image_path)

    if img is None:
        print('Error loading image')
        return

    # Preprocess the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    _, thresh_img = cv2.threshold(blurred_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    custom_config = r'--oem 3 --psm 6'
    recognized_text = pytesseract.image_to_string(thresh_img, lang='ara_number', config=custom_config)

    # Convert English digits to Arabic digits
    arabic_numerals = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
    recognized_text_arabic = recognized_text.translate(arabic_numerals)

    print(f"Recognized text (Arabic numerals): {recognized_text_arabic}")




   
    time.sleep(1)  # 1 second delay 


image_path = './imgae/0.png'

ocr_image(image_path)
