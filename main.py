from boilerplate.create_files import create_csv_file
from classes import JobScrapers as scraper
from flask import Flask, render_template, request, redirect, send_file


app = Flask("JobScrapper")
db = {}
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == "":
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        web3 = scraper.Web3JobScraper()
        web3.search_by_keyword(keyword)
        print(web3.get_all_jobs)
        bsu = scraper.BsuJobScraper()
        bsu.search_by_keyword(keyword)
        jobs = web3.get_all_jobs() + bsu.get_all_jobs()
        db[keyword] = jobs

        if len(jobs) == 0:
            return redirect("/?no_results=true")
    return render_template("search.html", keyword = keyword, jobs = jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    create_csv_file(f"{keyword}", db[keyword])
    return send_file(f"./files/{keyword}-jobs.csv", as_attachment = True)

app.run("0.0.0.0", debug=True)