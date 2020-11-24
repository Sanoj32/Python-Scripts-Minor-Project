from bs4 import BeautifulSoup
import requests
import json
from database import stored_links

def kantipurjob():
    links = []
    with open('C:/Projects/itjobseeker/public/jsondata/kathmandujob.json', 'r') as readfile:
        data = json.load(readfile)
    source = requests.get('https://kantipurjob.com/searchjob?category=25').text
    soup = BeautifulSoup(source,'lxml')
    temp = soup.find_all('div',class_='company-info-blk')
    for tem in temp:
        link = tem.h2.a['href']
        link = 'https://kantipurjob.com' + link
        links.append(link)
    for link in links:
        if link not in stored_links:
            print('New job found',link)
            source = requests.get(link).text
            soup = BeautifulSoup(source,'lxml')
            name = soup.find_all('div',class_='title')[1].get_text(strip=True)
            company = soup.find('div',class_='org-name').get_text(strip=True)
            level = soup.find('div',class_='posted-jobs-blk-list-blk').table.find_all('tr')[1].td.get_text(strip=True)
            salary = soup.find('div', class_='posted-jobs-blk-list-blk').table.find_all('tr')[1].find_all('td')[1].get_text(strip=True)
            address = soup.find('div', class_='posted-jobs-blk-list-blk').table.find_all('tr')[2].find_all('td')[0].get_text(strip=True)
            deadline = soup.find('div', class_='posted-jobs-blk-list-blk').table.find_all('tr')[4].find_all('td')[0].get_text(strip=True)
            deadline = deadline.split(',',1)[1]
            deadline = deadline.split('(', 1)[0]
            time = soup.find('div',class_='posted-jobs-blk-list-blk').table.find_all('tr')[0].find_all('td')[1].get_text(strip=True)
            experience = soup.find('div',class_='posted-jobs-blk-list-blk').table.find_all('tr')[2].find_all('td')[1].get_text(strip=True)
            vacancy = soup.find('div',class_='posted-jobs-blk-list-blk').table.find_all('tr')[3].find_all('td')[1].get_text(strip=True)
            desct = soup.find('div',class_='dashboard-section-right').get_text(strip=True)
            data.append({
                'name': name,
                'company': company,
                'vacancy': vacancy,
                'time': time,
                'address': address,
                'deadline': deadline,
                'experience': experience,
                'level': level,
                'salary': salary,
                'desct': desct,
                'Page_URL': link
            })
        else:
            print("Already in the database")

    with open('C:/Projects/itjobseeker/public/jsondata/kantipurjob.json', 'w') as outfile:
        json.dump(data, outfile)
        print("Kantipurjob done")




kantipurjob()