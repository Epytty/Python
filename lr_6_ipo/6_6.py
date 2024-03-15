'''Написать программу, которая выполняет парсинг страницы. Вывести на экран
информацию.'''

import requests
from bs4 import BeautifulSoup

url = 'https://newgrodno.by/'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

news = soup.find_all('div', class_='news-item')

for item in news:
    title = item.find('a', class_='news-title').text.strip()
    link = item.find('a', class_='news-title')['href']
    print(title)
    print(link)