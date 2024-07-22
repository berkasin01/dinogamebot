from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
from PIL import Image, ImageGrab

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
current_screen = pyautogui.screenshot(imageFilename="dino.png", region=(0, 350, 1920, 500))

px = current_screen.load()
print(px)
