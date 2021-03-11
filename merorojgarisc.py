import json

from datetime import datetime,timedelta

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH  = "C:\Program Files (x86)\Chromedriver\chromedriver.exe"
def merorojgarisc():
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


    driver = webdriver.Chrome(PATH)
    driver.get('https://www.merorojgari.com/')
    search = driver.find_element_by_xpath('//*[@id="post-13"]/div/div/form/div[1]/div[4]/span/span[1]/span/ul/li/input')
    search.send_keys('Information Technology')
    search.send_keys(Keys.RETURN)
    import time
    time.sleep(5)
    main = driver.find_element_by_xpath('//*[@id="post-13"]/div/div/ul')
    divs = main.find_elements_by_tag_name('a')
    for div in divs:
        link = div.get_attribute('href')
        links.append(link)
    driver.quit()

    for link in links:
        if link not in stored_links:
            print("New Job found!!!",link)
            source = requests.get(link).text
            soup = BeautifulSoup(source,'lxml')
            name = soup.find('h1',itemprop="headline").get_text(strip=True)
            time = soup.find('li', class_="job-type").get_text(strip=True)
            address = soup.find('li', class_="location").get_text(strip=True)
            company = soup.find('div', class_="company").p.strong.get_text(strip=True)
            desct = soup.find('div', class_="single_job_listing").get_text(strip=True)
            desct = desct.split('Similar Jobs:')[0]
            try:
                deadline = soup.find('li',class_='application-deadline').get_text(strip=True)
                deadline = deadline.split(':')[1]
                print(deadline)
            except:
                deadline = datetime.today() + timedelta(days=30)
                deadline = deadline.strftime('%Y/%m/%d')
            data.append({
                'name': name,
                'company': company,
                'time': time,
                'address': address,
                'deadline': deadline,
                'desct': desct,
                'Page_URL': link,
                'websitename': 'merorojgari.com'
            })
            print(deadline)
        else:
            print('Already in the database')
    with open('C:/Projects/itjobseeker/public/jsondata/merorojgari.json', 'w') as outfile:
        json.dump(data, outfile)
    print("merorojgari done")



merorojgarisc()