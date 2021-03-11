from bs4 import BeautifulSoup
import requests
import json


def kumarijob():
    links = []
    count = 0
    with open('C:/Projects/itjobseeker/public/jsondata/kumarijob.json', 'r') as readfile:
        try:
            data = json.load(readfile)
            stored_links = []
            for single_data in data:
                stored_links.append(single_data['Page_URL'])

        except:
            data = []
            stored_links = []
    sorurce = requests.get('https://www.kumarijob.com/jobs-by-category/62').text
    soup = BeautifulSoup(sorurce, 'lxml')

    var = soup.find_all('div', class_='job-detail')

    for i in var:
        link = i.h5.a['href']
        # print(link, "")
        links.append(link)
    for link in links:
        if link not in stored_links:
            stored_links.append(link)
            count += 1
            print("[" + str(count) + "]", "New job found ", link)
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'lxml')
            details = soup.find('div', class_='top-content-box')
            name = details.find('h3').get_text(strip=True)
            company = soup.find('div', class_='text-box').h5.get_text(strip=True)
            print(company, " company")
            otherdetails = details.find('ul', class_='job-detail-box')
            otherdetails = otherdetails.find_all('li')
            address = ""
            level = ""
            salary = ""
            experience = ""
            deadline = ""
            education = ""
            for detail in otherdetails:
                if detail.strong.get_text(strip=True) == "Job Location":
                    address = detail.span.get_text(strip=True)
                    continue
                if detail.strong.get_text(strip=True) == "Job Level":
                    level = detail.span.get_text(strip=True)
                    continue
                if detail.strong.get_text(strip=True) == "Salary":
                    salary = detail.span.get_text(strip=True)
                    continue
                if detail.strong.get_text(strip=True) == "Expiry date":
                    deadline = detail.span.get_text(strip=True)
                    print(deadline, " deadline")
                    continue
                if detail.strong.get_text(strip=True) == "Experience":
                    experience = detail.span.get_text(strip=True)
                    continue

            desct = soup.find('div', class_='left-content').get_text(strip=True)

            data.append({
                'name': name,
                'company': company,
                'level': level,
                'address': address,
                'salary': salary,
                'deadline': deadline,
                'education': education,
                'experience': experience,
                'desct': desct,
                'Page_URL': link,
                'websitename': 'kumarijob.com'
            })
        else:
            print("Already in the database")
    with open('C:/Projects/itjobseeker/public/jsondata/kumarijob.json', 'w') as outfile:
        json.dump(data, outfile)
    print("kumarijob done")



