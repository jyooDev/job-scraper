from file import create_csv_file
from extractors.extract_remoteOk_jobs import extract_remoteok_jobs
from extractors.extract_wwr_jobs import extract_wwr_jobs
from flask import Flask, render_template, request


app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    remoteok = extract_remoteok_jobs(keyword)
    print(remoteok)
    wwr = extract_wwr_jobs(keyword)
    jobs = remoteok + wwr
    return render_template("search.html", keyword = keyword, jobs = jobs)

app.run("0.0.0.0")