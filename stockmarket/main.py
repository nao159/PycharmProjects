import requests
import datetime as dt
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_ALPHA = "D9NHE85KYBYZD04D"
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": API_ALPHA
}
short_url = "https://www.alphavantage.co/query"
alpha_response = requests.get(short_url, params=alpha_params)
data = alpha_response.json()
time_data = data["Time Series (Daily)"]
time_data_list = [value for (key, value) in time_data.items()]
print(time_data_list[0])

now = dt.datetime.now().date()
yesterday = now - dt.timedelta(days=1)
two_days_ago = now - dt.timedelta(days=2)


yesterday_close_price = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])
two_days_ago_close_price = float(data["Time Series (Daily)"][f"{two_days_ago}"]["4. close"])
difference = yesterday_close_price - two_days_ago_close_price
percentage_diff = abs(float("{0:.2f}".format(difference / two_days_ago_close_price * 100)))

API_NEWS = "b74a5100103142c39000a0f0f6e146d3"

news_params = {
    "apiKey": API_NEWS,
    "from": yesterday,
    "q": "Tesla"
}
url = "https://newsapi.org/v2/everything"
news_response = requests.get(url, params=news_params)
news_data = news_response.json()
send_message = f"Difference in price between yesterday and 2 two days ago was {percentage_diff}%\n"
for i in range(0,3):
    author = f"Author: {news_data['articles'][i]['source']['name']}"
    title = news_data['articles'][i]['title']
    news_message = f"{author}\n{title}\n"
    send_message += news_message

news_slice = news_data['articles'][:3]
print(news_slice)
formatted_news_list = [f"{news['author']}: {news['title']}" for news in news_slice]
print(formatted_news_list)

#print(send_message)
with smtplib.SMTP("SMTP.gmail.com") as connection:
    connection.starttls()
    MY_MAIL = "vainikkaxd@gmail.com"
    MY_PASS = "031099ma"
    connection.login(user=MY_MAIL, password=MY_PASS)
    #connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg=send_message.encode('utf-8'))

