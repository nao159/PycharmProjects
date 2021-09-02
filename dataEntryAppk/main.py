from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from pprint import pprint
from time import sleep

GOOGLE_FORM_LINK = "https://forms.gle/xWdvJenCtb1KTug16"
PROPERTY_LINK = "https://realty.yandex.ru/sankt-peterburg/snyat/kvartira/studiya,1-komnatnie/?priceMax=22000"
CHROME_DRIVER_PATH = "C:\github\development\chromedriver.exe"
YANDEX_STARTER_LINK = "https://realty.yandex.ru/"
request = requests.get(url=PROPERTY_LINK)
data = request.text

list_of_offers = []

soup = BeautifulSoup(data, 'lxml')
all_link_elements = soup.find_all("li", class_="OffersSerpItem")
for link in all_link_elements:
    price_label = link.find("span", class_="price").text
    address_label = link.find("div", class_="OffersSerpItem__address").text
    link_label = link.find("a", class_="OffersSerpItem__link")['href']
    converted_link = f"{YANDEX_STARTER_LINK}{link_label}"
    time_to_metro = link.find("span", class_="MetroWithTime__distance").text
    closest_metro_station = link.find("span", "MetroStation__title").text
    new_value = {
        "price": price_label,
        'address': address_label,
        "link": converted_link,
        "time_to_metro": time_to_metro,
        "metro_station": closest_metro_station
    }
    list_of_offers.append(new_value)


def sort_by_time(offer):
    return offer['time_to_metro']


list_of_offers.sort(key=sort_by_time)

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url=GOOGLE_FORM_LINK)
pprint(list_of_offers)

for offer in list_of_offers:
    sleep(3)
    address_driver_label = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    address_driver_label.send_keys(offer['address'])
    price_driver_label = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_driver_label.send_keys(offer['price'])
    link_driver_label = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_driver_label.send_keys(offer['link'])
    time_to_metro_label = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input")
    time_to_metro_label.send_keys(offer["time_to_metro"])
    metro_station_label = driver.find_element_by_xpath(
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input")
    metro_station_label.send_keys(offer["metro_station"])
    button = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    button.click()
    sleep(1)
    retry_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    retry_button.click()
