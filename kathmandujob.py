from bs4 import BeautifulSoup
import requests
import json


def kathmandujob():
    links = []
    count = 0
    with open('C:/Projects/itjobseeker/public/jsondata/kathmandujob.json', 'r') as readfile:
        try:
            data = json.load(readfile)
            stored_links = []
            for single_data in data:
                stored_links.append(single_data['Page_URL'])

        except:
            data = []
            stored_links = []
    nums = [1, 14, 28, 42, 56]
    for num in nums:
        num = str(num)
        hyper_source = requests.get('https://kathmandujobs.com/jobs/' + num).text
        soup = BeautifulSoup(hyper_source, 'lxml')
        jobs = soup.find('div', class_='post-list')
        titles = jobs.find_all('div', class_='titles')
        for title in titles:
            link = title.find_all('a')[0]
            link = link['href']
            links.append(link)
        for link in links:
            if link not in stored_links:
                stored_links.append(link)
                count += 1
                source = requests.get(link).text
                soup = BeautifulSoup(source, 'lxml')
                job = soup.find('div', class_='details')
                name = job.find('div', class_='titles').h4.get_text(strip=True)
                company = job.find('div', class_='titles').h6.get_text(strip=True)
                experience = job.find_all('p', class_='address')[0].get_text(strip=True)
                experience = experience.split(':', 1)[1]
                level = job.find_all('p', class_='address')[1].get_text(strip=True)
                level = level.split(':', 1)[1]
                vacancy = job.find_all('p', class_='address')[2].get_text(strip=True)
                vacancy = vacancy.split(':', 1)[1]
                time = job.find_all('p', class_='address')[3].get_text(strip=True)
                time = time.split(':', 1)[1]
                salary = job.find_all('p', class_='address')[4].get_text(strip=True)
                salary = salary.split(':', 1)[1]
                education = job.find_all('p', class_='address')[5].get_text(strip=True)
                education = education.split(':', 1)[1]
                address = job.find_all('p', class_='address')[6].get_text(strip=True)
                address = address.split(':', 1)[1]
                deadline = job.find_all('p', class_='address')[7].get_text(strip=True)
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
                    'Page_URL': link,
                    'websitename': 'kathmandujobs.com'
                })
            else:
                print("Alredy in the database")
    with open('C:/Projects/itjobseeker/public/jsondata/kathmandujob.json', 'w') as outfile:
        json.dump(data, outfile)
        print("Kathmandu jobs done")
kathmandujob()