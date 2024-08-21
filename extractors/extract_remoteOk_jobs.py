import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
        })
    soup = BeautifulSoup(response.content, 'html.parser')
    all_jobs = []
    jobs = soup.find("table", id="jobsboard").find_all(
        "td", class_="company position company_and_position")
    for job in jobs:
        try:
            title = job.find("h2", itemprop="title").text
            company = job.find("h3", itemprop="name").text
            location = job.find("div", class_="location").text
            url = f'https://remoteok.com/{job.find("a", itemprop="url")["href"]}'
            job_data = {
                "title": title,
                "company": company,
                "region": location,
                "url": url,
            }           
            all_jobs.append(job_data) 
            print(job_data["url"])
        except AttributeError:
            pass
    return all_jobs