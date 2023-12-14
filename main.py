import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url = "https://www.championat.com/"
session = requests.Session()
      
try:
    push_req = session.get(url, headers=headers)
    if push_req.status_code == 200:
        soup = bs4(push_req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'news-item__content'})
        for div in divs:
            title = div.find('a').text
            link = div.find('a')['href']
            print(title)
            print('https://championat.com/' + link)
    else:
        print("Error")

except Exception:
    print("Введен несуществующий URL")


