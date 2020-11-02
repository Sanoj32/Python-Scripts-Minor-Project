from bs4 import BeautifulSoup
import  requests
import  json

def kumarijob():
    links = []
    data = []
    sorurce = requests.get('https://www.kumarijob.com/jobs/it_jobs').text
    soup = BeautifulSoup(sorurce, 'lxml')
    count = 0
    var = soup.find_all('a', class_='d-job')
    for i in var:
        link = i['href']
        links.append(link)
    for link in links:
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        details = soup.find('div', class_='job-title')
        name = details.find('h5').get_text(strip=True)
        company = details.find('p').get_text(strip=True)
        address = details.find_all('p')[1].get_text(strip=True)
        try:
            vacancy = soup.table.find_all('th', class_='left')[1].get_text(strip=True)
        except:
            vacancy = ""
        try:
            experience = soup.table.find_all('th', class_='left')[2].get_text(strip=True)
        except:
            experience = ""
        try:
            level = soup.table.find_all('th', class_='left')[4].get_text(strip=True)
        except:
            level = ""
        try:
            salary = soup.table.find_all('th', class_='left')[5].get_text(strip=True)
        except:
            salary = ""
        try:
            education = soup.table.find_all('th', class_='left')[6].get_text(strip=True)
        except:
            education = ""
        try:
            deadline = soup.table.find_all('th', class_='left')[7].get_text(strip=True)
        except:
            deadline = ""
        desct = soup.find('div', class_='left-side-content').get_text(strip=True)

        data.append({
            'name': name,
            'company': company,
            'level': level,
            'vacancy': vacancy,
            'address': address,
            'salary': salary,
            'deadline': deadline,
            'education': education,
            'desct': desct,
            'Page_URL': link
        })

    with open('C:/Projects/itjobseeker/public/jsondata/kumarijob.json', 'w') as outfile:
        json.dump(data, outfile)


