from bs4 import BeautifulSoup
import requests
import json
def merorojgari():
    source = requests.get('https://www.merorojgari.com/cat/information-technology/').text
    soup = BeautifulSoup(source, 'lxml')
    links = soup.find_all('a', class_='title-link')
    data = []
    for link in links:
        link = link['href']
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        name = soup.find('h1', class_='job-title').get_text(strip=True)
        company = soup.find('a', id='job_author_name').get_text(strip=True)
        time = soup.find('div', id='job_type').get_text(strip=True)
        desct = soup.find('div', class_='description').get_text(strip=True)


        data.append({
            'name': name,
            'company': company,
            'deadline': time,
            'desct': desct,
            'Page_URL': link
        })
    with open('C:/Projects/itjobseeker/public/jsondata/merorojgari.json', 'w') as outfile:
        json.dump(data, outfile)
    print("merorojgari done")


merorojgari()
