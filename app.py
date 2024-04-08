import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
    path = r'C:\Users\our_m\Downloads\chromedriver_win32\chromedriver.exe'
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  
    chrome_options.add_argument("webdriver.chrome.driver=" + path)
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = initialize_driver()

driver.get("http://sdetchallenge.fetch.com/")

leftbowl = [driver.find_element(By.ID, f'left_{i}') for i in range(9)]
rightbowl = [driver.find_element(By.ID, f'right_{i}') for i in range(9)]
goldbars = [driver.find_element(By.ID, f'coin_{i}') for i in range(9)]


def check(mid):
    goldbars[mid].click()
    time.sleep(5)
    try:
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print(f"Found the fake gold, it is number: {mid}")
    except:
        print("Do not close the alert manually!")  
    

low = 0
high = len(goldbars) - 1
flag = True
while low < high:
    mid = (high + low) // 2
    reset_button = driver.find_element(By.XPATH, "//button[@id='reset' and @class='button' and text()='Reset']")
    reset_button.click()

    time.sleep(3)
    if flag:
        add = 0
        flag =False
    else:
        add = 1

    for i in range(low, mid + add):
        leftbowl[i - low].send_keys(str(i))

    for i in range(mid + 1, high + 1):
        rightbowl[i - mid - 1].send_keys(str(i))

    driver.find_element(By.ID, "weigh").click()
    time.sleep(5)

    result_element = driver.find_element(By.XPATH, "//div[@class='result']/button[@id='reset' and @class='button']")
    result = result_element.text

    if result == "<":
        high = mid - 1 + add
    elif result == ">":
        low = mid + 1
    else:
        check(mid)
        break

check(low)
time.sleep(15)
driver.quit()
