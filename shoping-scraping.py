import requests
from bs4 import BeautifulSoup

url = 'https://www.n11.com/bilgisayar/dizustu-bilgisayar'

headersParams = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

response = requests.get(url,headers=headersParams).content

soup = BeautifulSoup(response,'html.parser')

list_li = soup.find_all('li',{'class' : 'column'},limit=5)

count = 1

for li in list_li:
    link = li.a.get('href')
    
    product_name = li.a.h3.text
    
    images = li.find('img',{'class' : 'cardImage'}).get('data-images').split(',')
    
    price = li.find('div', {'class' : 'priceContainer'}).find_all('span')[-1].ins.text
    
    print(f'{count}. product is {product_name} <---> {price}.')
    
    count += 1