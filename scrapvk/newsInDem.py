from bs4 import BeautifulSoup
import requests
from pprint import pprint


response = requests.get(url="https://news.ycombinator.com/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
storylinks = soup.find_all(name="a", class_="storylink")
s_o_upvote = soup.find_all(name="span", class_="score")
upvotes = [int(score.getText().split()[0]) for score in s_o_upvote]
texts = []
links = []
max_upvote_count = max(upvotes)
print(max_upvote_count)
index = upvotes.index(max_upvote_count)

for story in storylinks:
    s_o_link = story.get("href")
    links.append(s_o_link)
    s_o_text = story.getText()
    texts.append(s_o_text)


print(upvotes)
print(texts)
print(links)
print(texts[index])