import requests
from bs4 import BeautifulSoup

source = requests.get('https://kathmandujobs.com/jobs/1200').text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())