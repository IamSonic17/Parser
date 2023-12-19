import csv
import pytz
from datetime import datetime
import requests
from bs4 import BeautifulSoup as Bs4


def launch_parser():
    """
    This function collects headlines from website and add links
    to the full text of the news.
    """

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/119.0.0.0 Safari/537.36'
    }

    url = "https://www.championat.com/news/football/1.html?utm_source=button&utm_medium=news"
    session = requests.Session()

    try:
        push_req = session.get(url, headers=headers)
        if push_req.status_code == 200:
            soup = Bs4(push_req.content, 'html.parser')
            divs = soup.find_all('div', attrs={'class': 'news-item'})
            for div in divs:
                date_today = str(datetime.now(pytz.timezone('Europe/Moscow'))).split()[0]
                time = str(div.find('div', attrs={'class': 'news-item__time'}).text)
                title = div.find('a').text
                link = 'https://championat.com/' + str(div.find('a')['href'])
                flag = 0
                with open('data.csv', 'r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if title not in row:
                            flag = 1
                            continue
                        else:
                            flag = 0
                            break
                file.close()

                if flag == 1:
                    with open(f'data.csv', 'a', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            (
                                date_today,
                                time,
                                title,
                                link,
                            )
                        )
                    file.close()
        else:
            print("Error")

    except Exception:
        print("Введен несуществующий URL")


launch_parser()
