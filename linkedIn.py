from bs4 import BeautifulSoup
import  requests
import  json
from database import stored_links

def linkedin():

    data = []
    sorurce = requests.get(
        'https://www.linkedin.com/jobs/search/?f_TPR=r604800&geoId=104630404&keywords=developer').text
    soup = BeautifulSoup(sorurce, 'lxml')

    jobs = soup.find_all('ul')[12].find_all('li')

    for job in jobs:
        link = job.a['href']
        if link not in stored_links:
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'lxml')
            name = soup.find('h3', class_='sub-nav-cta__header').get_text(strip=True)
            company = soup.find('a', class_='sub-nav-cta__optional-url').get_text(strip=True)

            address = soup.find('span', class_='topcard__flavor topcard__flavor--bullet').get_text(strip=True)
            time = soup.find_all('span', class_='job-criteria__text job-criteria__text--criteria')[1].get_text(strip=True)
            desct = soup.find('main', class_='main').get_text(strip=True)
            deadline = soup.find('span', class_='posted-time-ago__text').get_text(strip=True)

            data.append({
                'name': name,
                'company': company,
                'address': address,
                'deadline': deadline,
                'desct': desct,
                'time':time,
                'Page_URL': link
            })
        else:
            print("Already in the database")
    with open('C:/Projects/itjobseeker/public/jsondata/linkedin.json', 'w') as outfile:
        json.dump(data, outfile)
    print("linkedin done")


