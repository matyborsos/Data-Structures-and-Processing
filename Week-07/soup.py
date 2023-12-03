import requests
from bs4 import BeautifulSoup

url = 'https://github.com/trending'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

repositories = soup.find_all('h1', class_='h3 lh-condensed')

assert isinstance(repositories, list)
assert len(repositories) > 1

for repo in repositories:
    title_element = repo.find('a')
    
    if title_element:
        title = title_element['href'].strip('/')
        link = f'https://github.com{title_element["href"]}'

        print(f'Title: {title}\nURL: {link}\n')