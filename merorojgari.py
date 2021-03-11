from bs4 import BeautifulSoup
import requests
import json


import mechanize
import urllib.request
import http.cookiejar

def merorojgari():
    links = []
    count = 0
    with open('C:/Projects/itjobseeker/public/jsondata/merorojgari.json', 'r') as readfile:
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
    # source = requests.get('https://www.merorojgari.com/cat/information-technology/').text
    # soup = BeautifulSoup(source, 'lxml')
    # vars = soup.find_all('h2', class_='title-job')
    # for var in vars:
    #     links.append(var.a['href'])
    #
    # for link in links:
    #     if link not in stored_links:
    #         stored_links.append(link)
    #         count += 1
    #         print("["+str(count) +"]" ,"New job found ", link)
    #         source = requests.get(link).text
    #         soup = BeautifulSoup(source, 'lxml')
    #         name = soup.find('h1', class_='job-title').get_text(strip=True)
    #         company = soup.find('a', id='job_author_name').get_text(strip=True)
    #         time = soup.find('div', id='job_type').get_text(strip=True)
    #         desct = soup.find('div', class_='description').get_text(strip=True)
    #         deadline = soup.find('div', class_='date').get_text(strip=True)
    #         data.append({
    #             'name': name,
    #             'company': company,
    #             'time': time,
    #             'deadline': deadline,
    #             'desct': desct,
    #             'Page_URL': link,
    #             'websitename': 'merorojgari.com'
    #         })
    #     else:
    #         print("Already in the database")
    # with open('C:/Projects/itjobseeker/public/jsondata/merorojgari.json', 'w') as outfile:
    #     json.dump(data, outfile)
    # print("merorojgari done")
