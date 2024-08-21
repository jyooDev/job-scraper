from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

class extract_wanted_jobs:
    def __init__(self, keyword):
        self.jobs_db = []
        self.scrape_dynamic_webpage(keyword)

    def scrape_dynamic_webpage(self, keyword):    
        p = sync_playwright().start()

        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")
        for x in range(5):
            page.keyboard.down("End")
            time.sleep(2)

        content = page.content()
        p.stop()
        self.scrape_jobs(content)

    def scrape_jobs(self, content):       
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__REty8")
        for job in jobs:
            link = f"https://www.wanted.co.kr/{job.find("a")["href"]}"
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company = job.find("span", class_="JobCard_companyName__N1YrF").text
            reward = job.find("span", class_="JobCard_reward__cNlG5").text
            job = {
                "Title": title,
                "Company": company,
                "Reward": reward,
                "Link": link
            }
            self.jobs_db.append(job)