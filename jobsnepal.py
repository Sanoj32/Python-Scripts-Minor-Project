from bs4 import BeautifulSoup
import requests
import json

def jobsnepal():
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
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml')

        company = soup.find('a', class_='text-white').get_text(strip=True)
        name = soup.find('h1', class_='job-title').get_text(strip=True)
        table_data = soup.find('table', class_='table-striped')
        vacancy = table_data.find_all('tr')[1].find_all('td')[1].get_text(strip=True)
        time = table_data.find_all('span', class_='font-weight-semibold')[1].get_text(strip=True)
        experience = table_data.find_all('tr')[3].span.get_text(strip=True)
        education = table_data.find_all('span', class_='font-weight-semibold')[3].get_text(strip=True)
        address = table_data.find_all('span', class_='font-weight-semibold')[4].get_text(strip=True)
        deadline = table_data.find_all('tr')[6].find_all('td')[1].get_text(strip=True)
        # try:
        #     desc = soup.find('div', class_='job-details-by-emloyer').find_all('ul')[1].get_text(strip=True)
        # except:
        #     desc = ""
        desct = soup.find('div', class_='col-lg-8').get_text(strip=True)

        data.append({
            'name': name,
            'company': company,
            'vacancy': vacancy,
            'time': time,
            'address': address,
            'deadline': deadline,
            'education': education,
            'experience':experience,
            # 'desc':desc,
            'desct':desct,
            'Page_URL': link
        })
    with open('C:/Projects/itjobseeker/public/jsondata/jobsnepal.json', 'w') as outfile:
        json.dump(data, outfile)
    print("jobsnepal done")






