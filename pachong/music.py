'''
https://music.163.com/discover/artist/cat?id=1003

https://music.163.com/artist?id=28387245
'''

import requests
from bs4 import BeautifulSoup
import csv
import random
import time
def get_artists(url):
    user_agent = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    }
    proxies = {
        'https': '113.138.212.133:13317'
    }
    # print(url)
    r = requests.get(url,headers=user_agent,proxies=proxies)
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    for item in soup.find_all('a', attrs={'class':'nm nm-icn f-thide s-fc0'}):
        artist_name = item.string.strip()
        artist_id = item['href'].replace('/artist?id=', '').strip()
        print(artist_id, artist_name)
        url = 'https://music.163.com/artist?id={}'.format(artist_id)
        # singers(url)
        user_agent = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
        }
        proxies = {
            'https': '113.138.212.133:13317'
        }

        try:
            r = requests.get(url, headers=user_agent,proxies=proxies, timeout=5)
            soup = BeautifulSoup(r.text, 'lxml')
            # print(soup)
            # 艺人信息
            singer = soup.find('meta',attrs={'property':'og:abstract'})['content']
            try:
                writers.writerow((artist_id, artist_name, singer, '组合'))
            except Exception as e:
                pass
            songlist = soup.select('.f-hide > li')[1:]
            for item in songlist:
                songname = item.string
                songid = str(item.find('a')['href']).split('=')[1]
                songname = songname.split('艺人介绍')[0].split('iPhone')[-1]

                a = "https://music.163.com/song?id="

                url = a + songid
                try:
                    r = requests.get(url, headers=user_agent,proxies=proxies, timeout=5)
                    soup = BeautifulSoup(r.text, 'lxml')
                    # print(soup)
                    sheet_id = str(soup.find_all('a', attrs={'class': 's-fc7'})[2]["href"]).split('=')[1]
                    sheet_name = str(soup.find_all('a', attrs={'class': 's-fc7'})[2].string)
                    img = str(soup.find('img', attrs={'class': 'j-img'})['data-src'])
                    print(sheet_id + ' ' + sheet_name + ' ' + img)
                    try:
                        writer.writerow((artist_id, artist_name, songid, songname, sheet_id, sheet_name, img, "英语"))
                    except Exception as e:
                        pass
                except Exception as e:
                    pass
        except Exception as e:
            pass


            # print(songid)
            # print(songname)

        print("**************************************************************************************")
        time.sleep(3)


def singers(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'referer': 'https://music.163.com/',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    songlist = soup.select('.f-hide > li')[1:]
    # print(songlist)
    for item in songlist:
        songname = item.string
        songid = str(item.find('a')['href']).split('=')[1]
        # songname = songname.split('艺人介绍')[0].split('iPhone')[-1]
        print(songid)
        print(songname)
        try:
            writer.writerow((songid, songname))
        except Exception as e:
            print(e)
    # print(soup)

if __name__ == '__main__':
    id_list = [2003]
    init_list = [-1]
    # 文件存储位置
    csvfile = open('music_163_artist.csv', 'a',newline='')
    writer = csv.writer(csvfile)
    writer.writerow(('artist_id', 'artist_name', 'songid', 'songname', 'sheet_id', 'sheet_name', 'img', "language"))

    csvfiles = open('singer.csv', 'a',newline='')
    writers = csv.writer(csvfiles)
    writers.writerow(('artist_id', 'artist_name', 'singer', 'sex'))

    for i in id_list:
        for j in init_list:
            url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(i, j)
            get_artists(url)