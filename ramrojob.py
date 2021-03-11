from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
import mechanize
import urllib.request
import http.cookiejar

def ramrojob():
    with open('C:/Projects/itjobseeker/public/jsondata/ramrojob.json','r') as readfile:
        try:
            data = json.load(readfile)
            stored_links = []
            for single_data in data:
                stored_links.append(single_data['Page_URL'])

        except:
            data = []
            stored_links = []
    cj = http.cookiejar.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://www.ramrojob.com/login")

    br.select_form(nr=0)
    br.form['email'] = 'sanoj.shrestha.13@gmail.com'
    br.form['password'] = 'ramrojobpass'
    br.submit()
    source = br.response().read()
    soup = BeautifulSoup(source, 'lxml')

    links = []
    temp_var = soup.find_all('h3', class_='job-listing-title')
    for temp in temp_var:
        link = temp.a['href']
        links.append(link)

    for link in links:
        if link not in stored_links:
            print("New job found!!",link)
            stored_links.append(link)
            source = requests.get(link).text
            soup = BeautifulSoup(source, 'lxml')
            name = soup.find('h1', itemprop="title").get_text(strip=True)
            address = soup.find('span', itemprop="addressLocality").get_text(strip=True)
            company = soup.find('h6', itemprop='hiringOrganization').get_text(strip=True)
            salary = soup.find('div', itemprop="baseSalary").get_text(strip=True)
            salary = salary.split(':')[1]
            deadline = soup.find('span', itemprop="validThrough").get_text(strip=True)
            try:
                time = soup.find('li', itemprop="employmentType").get_text(strip=True)
                time = time.split(':')[1]
            except:
                pass

            var = soup.find('ul', class_='job-detail-list').find_all('li')
            temp = "Opening"
            vacancy = ""
            level = ""
            for va in var:
                opening = va.strong.get_text(strip=True)
                if temp in opening:
                    vacancy = va.get_text(strip=True)
                    vacancy = vacancy.split(':')[1]
            temp = "Working Position"
            for va in var:
                job_level = va.strong.get_text(strip=True)
                if temp in job_level:
                    level = va.get_text(strip=True)
                    level = level.split(':')[1]

            desct = soup.find('div', class_='jobsearch-description').get_text(strip=True)
            data.append({
                'name': name,
                'company': company,
                'level': level,
                'vacancy': vacancy,
                'time': time,
                'address': address,
                'salary': salary,
                'deadline': deadline,
                'desct': desct,
                'Page_URL': link,
                'websitename': 'ramrojob.com'
            })
        else:
            print("Already in the database")

    with open('C:/Projects/itjobseeker/public/jsondata/ramrojob.json', 'w') as outfile:
        json.dump(data, outfile)
ramrojob()