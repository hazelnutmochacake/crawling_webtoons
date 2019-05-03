# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import requests
import re
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

webtoon_mon=[703846,
20853,
702608,
642653,
119874,
698918,
703307,
683496,
602287,
675554,
695321,
703852,
682637,
702672,
703850,
400739,
616239,
654138,
711422,
676695,
710758,
710750,
723046,
716857,
726214,
719899,
721433,
686312,
703855,
723007,
719508,
713289,
712901,
720810,
725831	,
626906	,
721456	,
722728

]

def cleanText(readData):
    #텍스트에 포함되어 있는 특수 문자 제거
    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text

def crawl_naver_webtoon(episode_url):
    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')

    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())

    if __name__ == "__main__":
        ep_title = cleanText(ep_title)
        comic_title = cleanText(comic_title)
        print(comic_title)
        print(ep_title)

    for img_tag in soup.select('.wt_viewer img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title, ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))

        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        print(image_file_path)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
        open(image_file_path, 'wb').write(image_file_data)

    print('Completed !')
for number in webtoon_mon:
  k=number
  # episode_url='https://comic.naver.com/webtoon/detail.nhn?titleId=%d&seq='%number
  for i in range(1150):
    if __name__ == '__main__':
      episode_url = 'https://comic.naver.com/webtoon/detail.nhn?titleId='+str(number)+'&seq=%d'  %i
    crawl_naver_webtoon(episode_url)

