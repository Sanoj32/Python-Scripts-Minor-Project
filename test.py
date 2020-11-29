from bs4 import BeautifulSoup
import requests

source = requests.get('https://merojob.com/category/it-telecommunication/?page=1').text
soup = BeautifulSoup(source,'lxml')
print(soup.prettify())