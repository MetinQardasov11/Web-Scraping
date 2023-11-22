import requests
from bs4 import BeautifulSoup

search_input = input('Enter the word you want to search: ').replace(' ', '+')
link = 'https://www.google.com/search?q=' + search_input

headerParams = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

response = requests.get(link,headers=headerParams)

soup = BeautifulSoup(response.content,'html.parser')

results = soup.find_all('div',class_='yuRUbf')

for div in results:
    anchor = div.find('a')
    link = anchor['href']
    text = anchor.find('h3').string
    print(link + '   <---->   ' + text)
    print('----------------------------------------------------------------')