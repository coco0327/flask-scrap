import requests
from bs4 import BeautifulSoup


class Scrap:
    def __init__(self, keyword):
        self.keyword = keyword
        self.url_list = [
            f"https://berlinstartupjobs.com/skill-areas/{self.keyword}",
            f"https://web3.career/{self.keyword}-jobs",
            f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={self.keyword}",
        ]
        self.results = []
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def find_job(self):
        response = requests.get(self.url_list[0], self.header)

        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
        for job in jobs:
            self.title = job.find("h4", class_="bjs-jlid__h").text
            self.company = job.find("a", class_="bjs-jlid__b").text
            self.link = job.find("h4", class_="bjs-jlid__h").find("a")["href"]

    def data_list(self):
        job_db = {
            "Title": self.title,
            "Company": self.company,
            "URL": self.link,
        }
        self.results.append(job_db)


class Scrap_web3(Scrap):
    def __init__(self, keyword):
        super().__init__(keyword)

    def find_job(self):
        response = requests.get(self.url_list[1], self.header)

        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find("tbody", class_="tbody").find_all("tr")
        for index, job in enumerate(jobs):
            if index == 4:
                continue
            self.title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary").text
            self.company = job.find("td", class_="job-location-mobile").find("h3").text
            self.link = f"https://web3.career{job.find("td", class_="job-location-mobile").find("a")["href"]}"
            
            
class Scrap_remoteok(Scrap):
    def __init__(self, keyword):
        super().__init__(keyword)
        
    def find_job(self):
        response = requests.get(self.url_list[2], self.header)
        
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("li", class_="feature")
        for job in jobs:
            self.title = job.find("span", class_="title").text
            self.company = job.find("span", class_="company").text
            self.link = job.find("a")


script = Scrap_remoteok("fullstack")
script.find_job()
