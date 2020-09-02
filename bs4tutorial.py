import requests
from bs4 import BeautifulSoup
import lxml


url = 'http://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')
title_tag = soup.find('h1')
title_and_author = title_tag.text
title_and_author = title_and_author.split('::')
title = title_and_author[0].rstrip()
author = title_and_author[1].lstrip()
print("Название : " + title)
print("Автор : " + author)