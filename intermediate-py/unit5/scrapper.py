import os
import urllib.request  # downloading
from urllib.parse import urljoin
from bs4 import BeautifulSoup  # parsing HTML

# u = urllib.request.urlopen('https://apod.nasa.gov/apod/archivepix.html').read()
# a_tags = (BeautifulSoup(u, 'lxml').findAll('a'))
# print(a_tags[0])
# tag = a_tags[0]
# print(tag["href"])

url = 'https://apod.nasa.gov/apod/archivepix.html'
download_directory = 'apod_pics'
content = urllib.request.urlopen(url)

for link in BeautifulSoup(content, 'lxml').findAll('a'):
    print('Following link:', link)
    href = urljoin(url, link['href'])

    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, 'lxml').findAll('img'):
        img_href = urljoin(href, img['src'])
        print('Downloading image:', img_href)
        img_name = img_href.split('/')[-1]
        urllib.request.urlretrieve(
            img_href, os.path.join(download_directory, img_name))
