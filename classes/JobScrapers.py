import requests
from bs4 import BeautifulSoup
from boilerplate import constants as c
from classes.Job import Job

class JobScraper():
    def __init__(self):
        self.all_jobs = []

    def get_soup(self, url : str, headers : str = None):
        response = requests.get(url) if headers is None else requests.get(url, headers={headers})
        return BeautifulSoup(response.text, "html.parser")
    
class BsuJobScraper(JobScraper):
    def __init__(self):
        super().__init__()

    def get_jobs(self, url):
        soup = super().get_soup(url, c.BSJ_REQUEST_HEADERS)
        jobs = soup.find_all("li", class_="bjs-jlid")
        for job in jobs:
            title = job.find("h4", class_="bjs-jlid__h").text
            company = job.find("a", class_="bjs-jlid__b").text
            description = job.find("div", class_="bjs-jlid__description").text
            link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]
            job = Job(title = title, company = company, description = description, link = link)
            self.all_jobs.append(job)
        return self.all_jobs
    
    def get_jobs_by_keyword(self, keyword: str):
        url = f"{c.BSJ_BASE_URL}{keyword}{c.BSJ_BASE_URL_SUFFIX}"
        self.get_jobs(url)

class Web3JobScraper(JobScraper):
    def __init__(self):
        super().__init__()

    # def is_job_open(self, url):
    #     soup = super().get_soup(url)
    #     try:
    #         soup.find("div", class_="mt-4 d-flex justify-content-center gap-3 mb-4")
    #         return True
    #     except AttributeError:
    #         return False

    def get_jobs(self, url):
        soup = super().get_soup(url)
        job_cards = soup.find_all("tr", class_="table_row")
        for job_card in job_cards:
            try:
                title = job_card.find("h2", class_="fs-6").text
                company = job_card.find("td", class_="job-location-mobile").find("h3").text
                region = job_card.find_all("td", class_="job-location-mobile")[1].text
                link = f"{c.WEB3__BASE_URL}{job_card.find("td", class_="job-location-mobile").find("a")["href"]}"
                # if self.is_job_open(link):
                job = Job(title = title, company = company, region = region, link = link)
                print(job)
                self.all_jobs.append(job)
            except AttributeError:
                pass
        return self.all_jobs
    
    def search_by_keyword(self, keyword: str):
        url = f"{c.WEB3__BASE_URL}/{keyword}{c.WEB3_BASE_URL_SUFFIX}"
        while True:
            print(f"Scraping {url}...")
            self.get_jobs(url)                                
            soup = super().get_soup(url)
            next_page_btn = soup.find("li", class_="page-item next")
            try:
                next_page_url = next_page_btn.find("a")["href"]
                url = f"{c.WEB3__BASE_URL}{next_page_url}"
                print(url)
            except AttributeError:
                break

 