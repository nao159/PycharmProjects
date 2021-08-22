import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_path = "C:\github\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_path)
url = "https://vk.com/id574060897"
driver.get(url=url)
email_field = driver.find_element_by_name("email")
email_field.send_keys("79026351382")
password_field = driver.find_element_by_name("pass")
password_field.send_keys("031099maX")
button = driver.find_element_by_css_selector("#quick_login_button")
button.click()
sleep(5)
navigation_list = driver.find_elements_by_class_name("side_bar_nav ol li")
for link in navigation_list:
    try:
        link.click()
        sleep(3)
    except selenium.common.exceptions.ElementNotInteractableException:
        link.text