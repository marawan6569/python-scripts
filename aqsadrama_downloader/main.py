import requests
from bs4 import BeautifulSoup as bs
import re
import sys


series_name = 'مسلسل الفدائي الجزء الثاني'
season_number = 2
exclude = []


def urls_list():
    from json import loads
    url_list = []
    with open('aqsadrama_site_map.json') as sitemap:
        json = loads(sitemap.read())
        for url in json['urlset']['url']:
            url_list.append(url['loc'])
    return url_list


def get_episode(text: str):
    text = text.replace('| أقصى دراما', '')
    episode_num = re.findall(r'\d\d', text)
    if episode_num:
        episode_num = int(episode_num[0]) if episode_num else None
    else:
        episode_num = re.findall(r'\d', text)
        episode_num = int(episode_num[0]) if episode_num else None
    return episode_num if series_name in text and episode_num not in exclude else False


urls = urls_list()

for url in urls:
    page = requests.get(url)
    soup = bs(page.content, "html.parser")
    title = soup.title
    video = soup.find('video')
    episode = get_episode(title.text)
    if episode:
        link = video.find('source').get('src')
        file_name = f"download/S0{season_number}E0{str(episode).zfill(2)}.{str(link).split('.')[-1]}"
        print('start => ', link)
        print(file_name)

        with open(file_name, "wb") as f:
            print("Downloading %s" % file_name)
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                    sys.stdout.flush()



