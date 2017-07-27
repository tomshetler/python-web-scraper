import requests
from bs4 import BeautifulSoup

def get_shower_thoughts():
    page = requests.get("https://www.reddit.com/r/Showerthoughts/")
    if page.status_code != 200:
        get_shower_thoughts()
    else:
        soup = BeautifulSoup(page.content, 'html.parser')

        shower_thoughts = list(soup.find_all('a', class_="title"))
        for thought in shower_thoughts:
            print(thought.get_text() + "\n")

        try:
            with open('shower_thoughts.txt', 'a+') as f:
                for thought in shower_thoughts:
                    f.write(str(thought.get_text().encode('utf8')))
                    f.write("\n")
        except FileNotFoundError:
            with open('shower_thoughts.txt', 'w') as f:
                for thought in shower_thoughts:
                    f.write(str(thought.get_text().encode('utf8')))
                    f.write("\n")

get_shower_thoughts()

