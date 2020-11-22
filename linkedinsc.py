import logging

import requests
from bs4 import BeautifulSoup
from linkedin_jobs_scraper import LinkedinScraper
from linkedin_jobs_scraper.events import Events, EventData
from linkedin_jobs_scraper.query import Query, QueryOptions, QueryFilters
from database import jsondata
import json
def linkedinsc():
    # Change root logger level (default is WARN)
    logging.basicConfig(level = logging.INFO)


    def on_data(data: EventData):
        # print('[ON_DATA]', data.title, data.company, data.date, data.link,data.seniority_level,data.employment_type)
        source = requests.get(data.link).text

        soup = BeautifulSoup(source, 'lxml')
        desct = soup.find('main', class_='main').get_text(strip=True)

        link = data.link
        link = link.split('?', 1)[0]
        print(link)
        jsondata.append({
                    'name': data.title,
                    'company': data.company,
                    'address': data.place,
                    'deadline': data.date,
                    'time': data.employment_type,
                    'Page_URL': link,
                    'desct':desct
                })

    def on_error(error):
        print('[ON_ERROR]', error)


    def on_end():
        print('[ON_END]')


    scraper = LinkedinScraper(
        chrome_options=None,  # You can pass your custom Chrome options here
        headless=True,  # Overrides headless mode only if chrome_options is None
        max_workers=1,  # How many threads will be spawned to run queries concurrently (one Chrome driver for each thread)
        slow_mo=0.4,  # Slow down the scraper to avoid 'Too many requests (429)' errors
    )

    # Add event listeners
    scraper.on(Events.DATA, on_data)
    scraper.on(Events.ERROR, on_error)
    scraper.on(Events.END, on_end)

    queries = [
        # Query(
        #     options=QueryOptions(
        #         optimize=True,  # Blocks requests for resources like images and stylesheet
        #         limit=50  # Limit the number of jobs to scrape
        #     )
        # ),
        Query(
            query='Developer',
            options=QueryOptions(
                locations=['Nepal'],
                optimize=True,
                limit=70,
                # filters=QueryFilters(
                #     company_jobs_url='https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000',  # Filter by companies
                #     relevance=RelevanceFilters.RECENT,
                #     time=TimeFilters.MONTH,
                #     type=[TypeFilters.FULL_TIME, TypeFilters.INTERNSHIP],
                #     experience=None,
                # )
            )
        ),
    ]

    scraper.run(queries)
    with open('C:/Projects/itjobseeker/public/jsondata/linkedin.json', 'w') as outfile:
        json.dump(jsondata, outfile)
        print("linkedin done")
