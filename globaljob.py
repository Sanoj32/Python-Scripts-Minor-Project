from bs4 import BeautifulSoup
import  requests
import json

def globaljob():
    data = []
    links = []
    hyper_source = requests.get('https://globaljob.com.np/category/it/it/630').text
    soup = BeautifulSoup(hyper_source, 'lxml')
    jobs = soup('div', class_='col-md-6')

    for job in jobs:
        link = job.a['href']
        links.append(link)


    for link in links:
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')
        name = soup.find('div', class_='headline').get_text(strip=True)
        details = soup.find('div', class_='vacancies-details')
        level = details.find_all('div', class_='row')[2].find_all('p')[2].get_text(strip=True)
        vacancy = details.find_all('div', class_='row')[3].find_all('p')[2].get_text(strip=True)
        salary = details.find_all('div', class_='row')[4].find_all('p')[2].get_text(strip=True)
        experience = details.find_all('div', class_='row')[5].find_all('p')[2].get_text(strip=True)
        time = details.find_all('div', class_='row')[6].find_all('p')[2].get_text(strip=True)
        deadline = details.find_all('div', class_='row')[7].find_all('p')[2].get_text(strip=True)
        try:
            deadline = details.find_all('div', class_='row')[8].find_all('p')[2].get_text(strip=True)
        except:
            pass
        print(deadline)
        education = soup.find('div', class_='elements').li.get_text(strip=True)
        # try:
        #     desc = soup.find('div', class_='elementss').ul.get_text(strip=True)
        #     desc1 = ""
        # except:
        #     desc1 = soup.find_all('div', class_='elementss')[1].get_text(strip=True)
        #     desc = ""
        desct = soup.find('div', class_='vacancies-details').get_text(strip=True)
        company = soup.find('section', class_='about-company').p.get_text(strip=True)
        address = soup.find('section', class_='about-company').find_all('p')[2].get_text(strip=True)

        data.append({
            'name': name,
            'company': company,
            'level': level,
            'vacancy': vacancy,
            'address': address,
            'salary': salary,
            'deadline': deadline,
            'time': time,
            'education': education,
            # 'desc': desc,
            # 'desc1': desc1,
            'desct': desct,
            'experience':experience,
            'Page_URL': link
        })

    with open('C:/Projects/itjobseeker/public/jsondata/globaljob.json', 'w') as outfile:
        json.dump(data, outfile)


globaljob()