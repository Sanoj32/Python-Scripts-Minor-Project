from bs4 import BeautifulSoup
import requests
import json
from database import stored_links

def jobsnepal():
    with open('C:/Projects/itjobseeker/public/jsondata/jobsnepal.json','r') as readfile:
        try:
            data = json.load(readfile)
        except:
            data = []
    hlink = []
    hlink.append('https://www.jobsnepal.com/category/information-technology-jobs')

    hyper_source = requests.get('https://www.jobsnepal.com/category/information-technology-jobs').text
    soup = BeautifulSoup(hyper_source, 'lxml')
    hyper_links = soup.find_all('a', class_='page-link')
    for hyperlink in hyper_links:
        var = hyperlink['href']
        hlink.append(var)
    hlink = list(dict.fromkeys(hlink))
    links = []
    for slink in hlink:
        source = requests.get(slink).text
        soup = BeautifulSoup(source, 'lxml')
        soup.find_all('a', class_='text-base')
        for i in soup.find_all('a', class_='text-base'):
            var = i['href']
            links.append(var)
    for link in links:
        if link not in stored_links:
            print("New job found !",link)
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'lxml')

            company = soup.find('a', class_='text-white').get_text(strip=True)
            name = soup.find('h1', class_='job-title').get_text(strip=True)
            table_data = soup.find('table', class_='table-striped')
            i_deadline = table_data.find_all('tr')
            education = ""
            experience = ""
            salary = ""
            level = ""
            for i in i_deadline:
                index = i.td.get_text(strip=True)
                if index == "Openings":
                    vacancy = i.find_all('td')[1].get_text(strip=True)
                elif index == "Salary":
                    salary = i.find_all('td')[1].get_text(strip=True)
                elif index == "Position Type":
                    time = i.find_all('td')[1].get_text(strip=True)
                elif index == "Position Level":
                    level = i.find_all('td')[1].get_text(strip=True)
                elif index == "Experience":
                    experience = i.find_all('td')[1].get_text(strip=True)
                elif index == "Education":
                    education = i.find_all('td')[1].get_text(strip=True)
                elif index == "Apply Before":
                    deadline = i.find_all('td')[1].get_text(strip=True)
                elif index == "City":
                    address = i.find_all('td')[1].get_text(strip=True)

            desct = soup.find('div', class_='col-lg-8').get_text(strip=True)
            print(link)
            data.append({
                'name': name,
                'company': company,
                'vacancy': vacancy,
                'time': time,
                'address': address,
                'deadline': deadline,
                'education': education,
                'experience':experience,
                'level':level,
                'salary':salary,
                'desct':desct,
                'Page_URL': link
            })
        else:
            print("Already in database")
    with open('C:/Projects/itjobseeker/public/jsondata/jobsnepal.json', 'w') as outfile:
        json.dump(data, outfile)
    print("jobsnepal done")


