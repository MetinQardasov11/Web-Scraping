from bs4 import BeautifulSoup

with open('index.html') as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc,"html.parser")

one_div = obj.find('div')

all_div = obj.find_all('div')

length_div = len(obj.find_all('div'))

second_div = obj.find_all('div')[1]

first_div_ul = obj.find_all('div')[0].ul

third_div_first_li = obj.find_all('div')[2].ul.find_all('li')[0]

print(one_div)

print(all_div)

print(length_div)

print(second_div)

print(first_div_ul)

print(third_div_first_li)


for div in obj.find_all('div'):
    if div.h2.a != None:
        print(div.h2.a.string.strip())
        
    else:
        print(div.h2.string.strip())
    

for a in obj.find_all('a'):
    print(a)