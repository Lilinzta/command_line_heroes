import requests
from bs4 import BeautifulSoup


def get_season_urls(season_div):
    ol_tag = season_div.find('ol', class_='mb-0 pl-2')
    links = ol_tag.find_all('a')
    urls = []
    for link in links:
        href = link.get('href')
        if href:
            full_url = href if href.startswith(
                'http') else f"https://www.redhat.com{href}"
            urls.append(full_url)
    return urls


def get_all_season_urls(soup):
    all_urls = []
    for season_num in range(1, 10):
        season_id = f'clhSeason{season_num}'
        season_div = soup.find('div', id=season_id)
        if season_div:
            season_urls = get_season_urls(season_div)
            all_urls.extend(season_urls)
    return all_urls


def get_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    all_urls = get_all_season_urls(soup)
    with open('url_of_episodes.txt', 'w', encoding='utf-8') as file:
        for i, url in enumerate(all_urls):
            if i == len(all_urls) - 1:
                file.write(url)
            else:
                file.write(url + '\n')
