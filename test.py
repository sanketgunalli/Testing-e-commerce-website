from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

# Initialize Chrome WebDriver (replace with Firefox WebDriver if needed)
chromedriver_path = "./chromedriver.exe"  # Adjust for your path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

def highlight_element(element):
    driver.execute_script("arguments[0].setAttribute('style', 'border: 6px solid red;');", element)
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', 'border: 0px;');", element)

# Open the website
driver.get("https://www.blossombookhouse.in/")
driver.maximize_window()
time.sleep(3)

person=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[2]/div[3]/div[5]/div[1]")
highlight_element(person)
person.click()
time.sleep(3)

person1=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[2]/div[3]/div[5]/div[2]/div/div/button[2]")
highlight_element(person1)
person1.click()
time.sleep(3)

email = driver.find_element(By.XPATH, "//*[@id='root-modal-popup']/div/div/div/form/div/div[1]/div[2]/input")
highlight_element(email)
email.send_keys("sanketgunalli@gmail.com")
time.sleep(3)

pwd = driver.find_element(By.XPATH, "//*[@id='root-modal-popup']/div/div/div/form/div/div[1]/div[3]/input")
highlight_element(pwd)
pwd.send_keys("Sanket@123")
time.sleep(5)

proceed = driver.find_element(By.XPATH, "//*[@id='root-modal-popup']/div/div/div/form/div/div[1]/div[6]/button")
highlight_element(proceed)
proceed.click()
time.sleep(5)


driver.execute_script("window.scrollBy(0,800)","")

b1=driver.find_element(By.XPATH,"//*[@id='__next']/main/div[3]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div/div/a")
highlight_element(b1)
b1.click()
time.sleep(3)


a1=driver.find_element(By.XPATH,"//*[@id='__next']/main/div/div/div[2]/div[2]/div[2]/span[2]/div/section/div/button")
highlight_element(a1)
a1.click()
time.sleep(3)

ct=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[2]/div[1]/div[1]/img")
highlight_element(ct)
ct.click()
time.sleep(3)


driver.execute_script("window.scrollBy(0,800)","")

b2=driver.find_element(By.XPATH,"//*[@id='__next']/main/div[3]/div[2]/div/div/div/div/div/div[2]/div[3]/div/div/div/div/a/img")
highlight_element(b2)
b2.click()
time.sleep(5)

a2=driver.find_element(By.XPATH,"//*[@id='__next']/main/div/div/div[2]/div[2]/div[2]/span[2]/div/section/div/button")
highlight_element(a2)
a2.click()
time.sleep(3)


cart=driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[2]/div[3]/div[3]/div[1]")
highlight_element(cart)
cart.click()
time.sleep(5)

co=driver.find_element(By.XPATH,"//*[@id='__next']/main/div/div/div/div[1]/div[3]/section[2]/div/a")
highlight_element(co)
co.click()
time.sleep(10)



