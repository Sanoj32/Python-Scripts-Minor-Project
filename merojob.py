from bs4 import BeautifulSoup
import requests
import json


def merojob():
    data = []
    hlink = []
    count = 1
    while count < 20:
        var = 'https://merojob.com/category/it-telecommunication/?page=' + str(count)
        count += 1
        hlink.append(var)


    for slink in hlink:
        try:
            print(slink)
            source = requests.get(slink).text
        except:
            break
        soup = BeautifulSoup(source, "lxml")
        links = []
        for i in soup.find_all('h1', class_="media-heading"):  # this gives the link of all the jobs in the pagination page
            link = i.a['href']
            link = "https://merojob.com" + link
            links.append(link)

        for link in links:  # this loops over those jobs on the pagination page
            source = requests.get(link).text
            soup = BeautifulSoup(source, "lxml")

            job = soup.find('div', class_='container my-3').find('div', class_='col-md-8')
            try:
                company = job.find('span', itemprop='name').get_text(strip=True)
            except:
                company = ""
            details = job.find_all('div', class_='card')[1]
            try:
                name = details.h1.get_text(strip=True)
            except:
                name = ""
            table_data = details.table

            try:
                level = table_data.find_all('tr')[1].find_all('td')[2].a.get_text(strip=True)
            except AttributeError:
                level = ""
            try:
                vacancy = table_data.find_all('tr')[2].strong.get_text(strip=True)
            except:
                vacancy = ""
            try:
                time = table_data.find('td', itemprop='employmentType').get_text(strip=True)
            except:
                time = ""
            try:
                address = table_data.find('span', class_='clearfix').get_text(strip=True)
            except:
                address = ""
            try:
                salary = table_data.find_all('tr')[5].find_all('td')[2].get_text(strip=True)
            except:
                salary = ""
            try:
                deadline = table_data.find_all('tr')[6].find_all('td')[2].get_text(strip=True)
            except:
                deadline = ""
            try:
                education = soup.find('span', itemprop='educationRequirements').get_text(strip=True)
            except:
                education = ""
            try:
                skills = soup.find('span', itemprop='skills').get_text(strip=True)
            except:
                skills = ""
            # try:
            #     desc = soup.find('div', 'card-text p-2').ul.get_text(strip=True)
            # except:
            #     desc = ""
            # try:
            #     desc1 = soup.find_all('div', itemprop='description')[2].get_text(strip=True)
            # except:
            #     desc1 = ""
            desct = soup.find_all('div', class_='col-md-8')[1].find_all('div', class_='card-body')[1].get_text(strip=True)
            print(desct)
            data.append({
                'name': name,
                'company': company,
                'level': level,
                'vacancy': vacancy,
                'time': time,
                'address': address,
                'salary': salary,
                'deadline': deadline,
                'education': education,
                'skills': skills,
                # 'desc': desc,
                # 'desc1': desc1,
                'desct': desct,
                'Page_URL': link
            })

    with open('C:/Projects/itjobseeker/public/jsondata/merojob.json', 'w') as outfile:
        json.dump(data, outfile)
    print("merojob done")
