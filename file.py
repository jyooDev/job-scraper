import csv

def create_csv_file(file_name, jobs):
        file = open(
            file=f"{file_name}-jobs.csv",
            mode="w",
            encoding="utf-8"
            )
        # row as list
        writer = csv.writer(file)  
        #first row entered becomes header row by default
        writer.writerow(jobs[0].keys())
        #get the values of each job as list and write row
        for job in jobs:
            writer.writerow(job.values())
        file.close()
