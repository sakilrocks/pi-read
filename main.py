
import os
import time
import subprocess
import RPi.GPIO as GPIO
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

# switch physical pin 12
GPIO.setmode(GPIO.BOARD)
switch_pin = 12

GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# text to speech
def speak(text):
    if not text.strip():
        return

    safe_text = text.replace("\n", " ").replace('"', "").strip()
    print(f"speaking: {safe_text}")
    subprocess.run(["espeak", "-s", "120", safe_text])


# image preprocessing
def process_image(photopath):
    photopath = "photo.jpg"

    img = Image.open(photopath)
    img = img.convert("L")  # grayscale

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    img = img.filter(ImageFilter.EDGE_ENHANCE)

    img.save("processed.jpg")


# OCR + speech
def ocr_and_speak():
    speak("processing image.")
    process_image("photo.jpg")

    speak("detecting text.")
    text = subprocess.getoutput("tesseract processed.jpg stdout").strip()

    print("detected text:", text)

    if text:
        time.sleep(1)
        speak("here's the output.")
        time.sleep(0.5)
        speak(text)
    else:
        speak("no readable text found.")

    time.sleep(0.5)
    speak("ready for next capture.")


# main loop
speak("system is ready. press the button to capture.")
print("click the button")

try:
    while True:

        if GPIO.input(switch_pin) == GPIO.LOW:  # button pressed
            speak("clicking picture")
            print("clicking picture")

            subprocess.run(["rpicam-still", "-n", "-o", "photo.jpg"])

            for _ in range(10):
                if os.path.exists("photo.jpg"):
                    break
                time.sleep(0.5)

            if not os.path.exists("photo.jpg"):
                speak("failed to capture image.")
                continue

            ocr_and_speak()

            while GPIO.input(switch_pin) == GPIO.LOW:
                time.sleep(0.1)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    speak("program stopped.")