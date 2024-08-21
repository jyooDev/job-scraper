from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests

def extract_wwr_jobs(keyword):
    url = f"https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

    all_jobs = []
    for job in jobs:
        try:
            title = job.find("span", class_="title").text
            company = job.find("span", class_="company").text
            location = job.find("span", class_="region").text if job.find("span", class_="region") is not None else "N/A"
            url = f'https://weworkremotely.com/{job.find("div", class_="tooltip--flag-logo").next_sibling["href"]}'
            job_data = {
                "title": title,
                "company": company,
                "location": location,
                "url": url,
            }
            all_jobs.append(job_data)
        except AttributeError:
            pass    
    
    return all_jobs