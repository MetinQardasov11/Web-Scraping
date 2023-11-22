import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://sadikturan.com'

response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

courses = soup.find_all(class_='kurs')

with open('courses.csv','w') as csv_file:
    csv_writer = writer(csv_file)
    
    csv_writer.writerow(['course_image','course_name','course_feedback','udemy_link','site_link'])
    
    for course in courses:
        image_link = course.find('img')['src']
        
        course_name = course.find(class_='media-body').find('h2').string
        
        course_feedback = course.find(class_='media-body').find('span').string

        links = soup.find(class_='card-footer').find_all('div')[1].find_all('a')
        
        course_udemy_link = links[0]['href']
        
        course_site_link = url + links[1]['href']
        
        csv_writer.writerow([image_link,course_name,course_feedback,course_udemy_link,course_site_link])