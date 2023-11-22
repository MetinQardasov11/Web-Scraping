from bs4 import BeautifulSoup

with open('index.html') as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc,"html.parser")

result_1 = obj.div

result_2 = obj.find('div')

result_3 = obj.find(id='div2')

result_4 = obj.find(class_='group3')

result_5 = obj.select('#header')

result_6 = obj.select('#div1')

result_7 = obj.select('.section')

result_8 = obj.select('.section')[0]

# OR

result_8_same = obj.select_one('.section')

result_9 = obj.div.attrs

div1_id = obj.div.attrs['id']

div1_class = obj.div.attrs['class']

all_text = obj.get_text(strip=True,separator=',')

print(result_1.prettify())

print(result_2.prettify())

print(result_3.prettify())

print(result_4.prettify())

print(result_5)

print(result_6)

print(result_7)

print(result_8)

print(result_8_same)

print(result_9)

print(div1_id)

print(div1_class)

print(all_text)

for a in obj.find_all('a'):
    print(a.get('href'))
# OR
print('-------------------------')
for a in obj.find_all('a'):
    print(a['href'])