import requests

url_pattern = 'http://tululu.org/txt.php?id='
for book_id in range(1, 11):
    print(book_id)
    url = f"{url_pattern}{book_id}"
    print(url)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 301:
        continue
    response.raise_for_status()
    file_name = 'id' + str(book_id) + '.txt'
    with open(file_name, "w") as my_file:
        my_file.write(response.text)

