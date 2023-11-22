import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250'

headersParams = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0'
}

response = requests.get(url,headers=headersParams).content

soup = BeautifulSoup(response,'html.parser')

ul = soup.find('ul',{'class':'ipc-metadata-list'})

li_list = ul.find_all('li',limit=10)

for item in li_list:
    movie_name = item.find('h3',{'class' : 'ipc-title__text'}).text
    
    point = item.find('span', {'class' : 'ipc-rating-star'}).text
    
    print(movie_name + ' <---> ' + point)
    