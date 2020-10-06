import requests
from bs4 import BeautifulSoup
import lxml
import os
from pathvalidate import sanitize_filename
from pathvalidate import sanitize_filepath
import urllib


def download_txt(download_url, title, folder='books/'):
    response = requests.get(download_url)
    folder = sanitize_filepath(folder)
    file_name = sanitize_filename(title) + '.txt'
    filepath = os.path.join(folder, file_name)
    with open(filepath, "w") as my_file:
        my_file.write(response.text)

    return filepath

def download_image(image_url, picture, book_id, folder='previews/'):
    response = requests.get(image_url)
    if picture == '/images/nopic.gif':
        file_name = 'nopic'+ str(book_id) + '.gif'
        pass
    else:
        file_name = str(book_id) + '.jpg'
    filepath = os.path.join(folder, file_name)
    with open(filepath, "wb") as my_file:
        my_file.write(response.content)


url_pattern = 'https://tululu.org/'
for book_id in range(1,11):
    url = f"{url_pattern}b{book_id}/"
    download_url = ''
    response = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(response.text, 'lxml')
    try:
        download_link_tag = soup.find('table', class_='d_book').find_all('a')
    except AttributeError:
        continue
    for link in download_link_tag:
        if 'txt' in link['href']:
            download_link = link['href']
            download_url = f"{url_pattern}{download_link}"
    if response.status_code == 302:
        continue
    try:
        title_tag = soup.find('div', id='content').find('h1')
    except AttributeError:
        continue
    title_and_author = title_tag.text
    title_and_author = title_and_author.split('::')
    title = title_and_author[0].rstrip()
    picture = soup.find('div', class_='bookimage').find('img')['src']
    comment_section_tag = soup.find('div', id='content').find_all('div', class_='texts')
    print(comment_section_tag)
    #comment_tag = comment_section_tag.find_all('span', class_='black')
    #print(comment_tag)
    #except AttributeError:
        #continue
    #comment = comment_tag.text
    #print(title)
    #print(comment)
    #image_url = urllib.parse.urljoin(url_pattern, picture)
    #if download_url:
        #download_txt(download_url, title, 'books/')
    #download_image(image_url, picture, book_id)
