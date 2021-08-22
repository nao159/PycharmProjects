from selenium import webdriver

chrome_driver_path = "C:\github\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
date = driver.find_elements_by_css_selector(".event-widget ul li time")
event = driver.find_elements_by_css_selector(".event-widget ul li a")
converted_date = []
converted_event = []
for element in date:
    c_element = element.text
    converted_date.append(c_element)
    print(element.text)
for element in event:
    c_element = element.text
    converted_event.append(c_element)
    print(element.text)
new_dict = dict(zip(converted_date, converted_event))
print(new_dict)




driver.close()
driver.quit()