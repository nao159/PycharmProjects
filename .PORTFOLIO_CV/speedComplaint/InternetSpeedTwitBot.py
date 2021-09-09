from selenium import webdriver
from time import sleep

chrome_driver_path = "C:\github\development\chromedriver.exe"
speed_test_website_checker = "https://www.speedtest.net/"
twitter_login_page = "https://twitter.com/login"
promised_down = 150
promised_up = 20
TWITTER_EMAIL = "vainikkaxd@gmail.com"
TWITTER_PASSWORD = "031099maX"


class InternetSpeedTwitBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = promised_up
        self.down = promised_down

    def get_internet_speed(self):
        self.driver.get(url=speed_test_website_checker)
        check_button = self.driver.find_element_by_class_name("start-text")
        check_button.click()
        sleep(60)
        result_down = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        result_up = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.current_down = result_down.text
        self.current_up = result_up.text
        print(result_up.text)
        print(result_down.text)

    def tweet_at_provider(self):
        sleep(3)
        self.driver.get(url=twitter_login_page)
        email_field = self.driver.find_element_by_name("session[username_or_email]")
        email_field.send_keys(TWITTER_EMAIL)
        password_field = self.driver.find_element_by_name("session[password]")
        password_field.send_keys(TWITTER_PASSWORD)
        next_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        next_button.click()
        #next_button = self.driver.find_element_by_link_text("Next")
        #next_button.click()
        sleep(3)
        #password_field = self.driver.find_element_by_name("password")
       # password_field.send_keys(TWITTER_PASSWORD)
        sleep(5)
        twit_field_page = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')

        twit_field_page.send_keys(f"My current internet speed is equal to {self.current_up} up Mb/s and {self.current_down} down Mb/s while it should be {self.up}/{self.down}")
        twit_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        twit_button.click()
        sleep(3)
        self.driver.close()

    def finish(self):
        self.driver.quit()

