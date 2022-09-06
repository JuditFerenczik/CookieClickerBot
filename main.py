from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

minutesToPlay = input("How many minutes do you want to play?")
try:
    minutesToPlay = float(minutesToPlay)
    continueToPlaying = True
except:
    print("Input wasnt a number!!")
    continueToPlaying = False
if continueToPlaying:
    service = Service("C:\Development\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get("https://orteil.dashnet.org/cookieclicker/")
    start = time.time()
    end = time.time()
    fullTime = end - start
    time.sleep(2)
    try:
        lang = driver.find_element(By.CSS_SELECTOR, "#promptContentChangeLanguage .langSelectButton")
        lang.click()
        cookies = driver.find_element(By.LINK_TEXT,"Got it!")
        cookies.click()
    except:
        print("lang is not there")
    time.sleep(2)
    button = driver.find_element(By.ID, "bigCookie")
    while  (fullTime < 60*minutesToPlay):
        button.send_keys(Keys.ENTER)
        end = time.time()
        if (end - start) > 5:
            fullTime += end - start
            start = end
            print("Buy sth")
            #extraHelp = driver.find_elements(By.CSS_SELECTOR, "#products .product")
            #extraHelp = [helper.text for helper in extraHelp ]
            extraPrice = driver.find_elements(By.CSS_SELECTOR, "#products .product.unlocked .price")
            extraPrice = [price.text.replace(',','') for price in extraPrice]
            extraPrice = [0.0 if price == '' else float(price) for price in extraPrice]
            if len(extraPrice) > 0:
                maxPrice = max(extraPrice)
                indexPrice = extraPrice.index(maxPrice)
                print(maxPrice, " in place of ",indexPrice)
                print(extraPrice)
                print(fullTime)
                idSelector = f"product{indexPrice}"
                elementToClick = driver.find_element(By.ID, idSelector)
                elementToClick.click()