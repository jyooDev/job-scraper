import csv
from dataclasses import asdict

def create_csv_file(file_name, jobs):
    with open(
        file=f"./files/{file_name}-jobs.csv",
        mode="w",
        encoding="utf-8",
        newline = ""
    ) as file:
    
        # convert the list of Job dataclasses to a list of dictionary
        jobs_dict = [asdict(job) for job in jobs]
        writer = csv.DictWriter(file, fieldnames=jobs_dict[0].keys())  
        # first row entered becomes header row by default
        writer.writeheader()
        writer.writerows(jobs_dict)