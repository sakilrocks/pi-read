# pi-read

a Raspberry Pi project that captures an image, extracts text using OCR, and reads the detected text aloud.   
This system is designed to help convert printed text into speech using a camera and a physical button trigger.

---

## Features

- Capture image using Raspberry Pi camera
- Image preprocessing to improve OCR accuracy
- Text recognition using Tesseract OCR
- Text to speech output using eSpeak
- Physical button trigger via GPIO
- Fully offline system

---

## How It Works

1. The system waits for a button press.
2. When the button is pressed:
   - A photo is captured using the Raspberry Pi camera.
3. The image is processed:
   - Converted to grayscale
   - Contrast enhanced
   - Edge enhancement applied
4. Tesseract OCR detects text in the image.
5. The detected text is spoken aloud using eSpeak.

---

## Hardware Requirements

- Raspberry Pi
- Raspberry Pi Camera Module
- Push Button
- Jumper Wires
- Speaker or audio output

---

## Software Requirements

- Python 3
- Tesseract OCR
- eSpeak
- Pillow
- RPi.GPIO
