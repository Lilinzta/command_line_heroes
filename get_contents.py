import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote


def get_contents():
    if not os.path.exists('en_contents'):
        os.makedirs('en_contents')
    with open('url_of_episodes.txt', 'r', encoding='utf-8') as url_file:
        urls = [line.strip() for line in url_file.readlines()]
    for url_index, url in enumerate(urls):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find('div', class_='tab-content')
        p_tags = content_div.find_all('p')
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip('/').split('/')
        filename = f"{unquote(path_parts[-2])}_{unquote(path_parts[-1])}.txt"
        filename = filename.replace('/', '_').replace('\\', '_')
        output_filepath = os.path.join('en_contents', filename)
        with open(output_filepath, 'w', encoding='utf-8') as file:
            for i, p_tag in enumerate(p_tags):
                p_text = p_tag.get_text(strip=True)

                if i == len(p_tags) - 1:
                    file.write(p_text)
                else:
                    file.write(p_text + '\n\n')
