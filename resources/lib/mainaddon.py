import requests
import re
from bs4 import BeautifulSoup

def get_soup(URL0):
    page = requests.get(URL0)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=16):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
