from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
import keyboard
from PIL import Image, ImageGrab
import numpy

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_settings)

url = "https://elgoog.im/dinosaur-game/"

driver.get(url=url)
driver.maximize_window()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, value='button[mode="primary"]').click()
pyautogui.press('space')

time.sleep(2)
game_on = True
while game_on:
    if keyboard.is_pressed("esc"):
        game_on = False
    current_screen = pyautogui.screenshot(imageFilename="dino.png", region=(0, 350, 1920, 500))
    area_to_search = pyautogui.screenshot(imageFilename="tree.png", region=(210, 300, 170, 450))
    img = Image.open("tree.png")

    numpy_arr = numpy.array(img)
    if numpy.count_nonzero(numpy_arr < 84) > 100:
        pyautogui.press("space")


