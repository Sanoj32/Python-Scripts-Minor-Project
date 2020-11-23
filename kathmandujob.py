from bs4 import BeautifulSoup
import requests
import json
from database import stored_links

def kathmandujob():
    links = []
    with open('C:/Projects/itjobseeker/public/jsondata/kathmandujob.json', 'r') as readfile:
        data = json.load(readfile)
    hyper_source = requests.get('https://kathmandujobs.com/jobs/1').text
    soup = BeautifulSoup(hyper_source, 'lxml')
    jobs = soup.find('div', class_='post-list')
    titles = jobs.find_all('div',class_='titles')
    for title in titles:
        link = title.find_all('a')[0]
        link = link['href']
        links.append(link)
    for link in links:
        if link not in stored_links:
            print("New job found",link)
            source = requests.get(link).text
            soup = BeautifulSoup(source,'lxml')
            job = soup.find('div',class_='details')
            name = job.find('div',class_='titles').h4.get_text(strip=True)
            company = job.find('div',class_='titles').h6.get_text(strip=True)
            experience = job.find_all('p',class_='address')[0].get_text(strip=True)
            experience = experience.split(':', 1)[1]
            level = job.find_all('p', class_='address')[1].get_text(strip=True)
            level = level.split(':', 1)[1]
            vacancy = job.find_all('p', class_='address')[2].get_text(strip=True)
            vacancy = vacancy.split(':', 1)[1]
            time = job.find_all('p',class_='address')[3].get_text(strip=True)
            time = time.split(':', 1)[1]
            salary = job.find_all('p',class_='address')[4].get_text(strip=True)
            salary = salary.split(':', 1)[1]
            education = job.find_all('p',class_='address')[5].get_text(strip=True)
            education = education.split(':', 1)[1]
            address = job.find_all('p',class_='address')[6].get_text(strip=True)
            address = address.split(':', 1)[1]
            deadline = job.find_all('p',class_='address')[7].get_text(strip=True)
            deadline = deadline.split(':', 1)[1]
            desct = job.get_text(strip=True)
            data.append({
                'name': name,
                'company': company,
                'vacancy': vacancy,
                'time': time,
                'address': address,
                'deadline': deadline,
                'education': education,
                'experience': experience,
                'level': level,
                'salary': salary,
                'desct': desct,
                'Page_URL': link
            })
        else:
            print("Alredy in the database")
    with open('C:/Projects/itjobseeker/public/jsondata/kathmandujob.json', 'w') as outfile:
        json.dump(data, outfile)

kathmandujob()