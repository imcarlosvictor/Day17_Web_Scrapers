from bs4 import BeautifulSoup
import requests
from typing import List


url = 'https://www.google.com/finance'
source = requests.get(url)

# Display Status Code
status = source.status_code
print(f'STATUS CODE: {status}\n')

soup = BeautifulSoup(source.text, 'lxml')


def find_stock(*position: int) -> str:
    """Lists the most followed stocks shown on Google Finance.

    Args:
        position: Number of popular stocks listed (6)

    Returns:
        A string displaying the company, symbol, following and percent change.
    
    """

    for num in position:
        stock_block = soup.find_all(class_='QE2JIe')

        # Company Info
        company_name = stock_block[num].find(class_='TwnKPb')
        stock_symbol = stock_block[num].find(class_='COaKTb')

        # Following
        user_following = stock_block[num].find(class_='Iap8Fc')

        # Stock Percent
        percent = stock_block[num].find(class_='JwB6zf')
        percent_change = percent.find('path').get('d')
        increase = 'M4 12l1.41 1.41L11 7.83V20h2V7.83l5.58 5.59L20 12l-8-8-8 8z'

        if percent_change == increase:
            print(f'{company_name.get_text()} [{stock_symbol.get_text()}] \n{user_following.get_text()}\t +{percent.get_text()}\n')
        elif percent_change != increase:
            print(f'{company_name.get_text()} [{stock_symbol.get_text()}] \n{user_following.get_text()}\t -{percent.get_text()}\n')


find_stock(0,1,2,3,4,5)