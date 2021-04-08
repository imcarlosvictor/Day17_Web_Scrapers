from bs4 import BeautifulSoup as bs
import requests

source = requests.get('https://www.cbc.ca/news/canada/toronto')
print(f'STATUS CODE: [{source.status_code}]')

# Parse raw HTML
soup = bs(source.text, 'lxml')

# Search for info
news_headlines = soup.find_all('h3', class_='headline')
news_timestamp = soup.find_all('time', class_='timeStamp')
# news_link = soup.find_all('a', class_='contentWrapper')

info_grouping = zip(news_headlines, news_timestamp)
info_grouping = list(info_grouping)

for news, timestamp in info_grouping:
    print(f'DATE: {timestamp.string}, TITLE: {news.string}')