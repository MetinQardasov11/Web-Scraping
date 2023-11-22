from bs4 import BeautifulSoup

with open('index.html') as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc,"html.parser")

result = obj.prettify()
# print(result)

title = obj.title

title_name = obj.title.name

title_string = obj.title.string

body = obj.body

h1 = obj.body.h1

div = obj.body.div

ul = obj.ul

li = obj.ul.li

print(title)

print(title_name)

print(title_string)

print(body.prettify())

print(h1)

print(div.prettify())

print(ul.prettify())

print(li.prettify())