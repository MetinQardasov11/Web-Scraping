from bs4 import BeautifulSoup

with open('index.html') as file:
    html_doc = file.read()

obj = BeautifulSoup(html_doc,"html.parser")

result_head = obj.head

result_body = obj.body

body_content = obj.body.div.contents

fourth_body_content = obj.body.div.contents[3]

li_content = obj.body.div.contents[3].contents

second_li_content = obj.body.div.contents[3].contents[1]

print(result_head)

print(result_body)

print(body_content)

print(fourth_body_content)

print(li_content)

print(second_li_content)

for child in obj.body.div.children:
    if child != '\n':
        print(child)
        

for descendant in obj.body.div.descendants:
    if descendant != '\n':
        print(descendant)
        

h2 = obj.body.h2

div = h2.parent

li = obj.body.li

ul = li.parent

div2 = div.next_sibling.next_sibling

print(h2)

print(div)

print(ul)

print(li)

print(div2)

third_li = obj.find(class_='third li')

second_li = third_li.previous_sibling.previous_sibling

first_li = second_li.find_previous_sibling('li')

first_and_second_li = third_li.find_previous_siblings('li')

ul_first = first_li.parent

div_first = first_li.parent.parent

print(third_li)

print(second_li)

print(first_li)

print(first_and_second_li)

print(ul_first)

print(div_first)