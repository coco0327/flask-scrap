from flask import Flask, render_template, request, redirect, send_file


app = Flask("Job Scrapper")

db = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        job_db = db[keyword]

    return render_template("search.html", keyword=keyword, job_db=jobs)


app.run()
