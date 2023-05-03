import RPi.GPIO as GPIO
from selenium import webdriver

def leave_room():
    driver = webdriver.Chrome()
    url = ""
    driver.get(url)
    button = driver.find_element_by_class_name("leaveroom")
    button.click()

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(17) == True:
        leave_room()
