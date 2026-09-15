import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
import re

class JobScraper:
    def __init__(self, url):
        self.url = url
        self.jobs_data = []

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"Error vachindi: {e}")
            return None

    def parse_jobs(self, html_content):
        if not html_content:
            return
        
        soup = BeautifulSoup(html_content, "html.parser")
        cards = soup.find_all("div", class_="card-content")

        experience_levels = ["Entry-Level", "Mid-Level", "Senior-Level"]
        work_modes = ["Remote", "Hybrid", "On-site"]

        for card in cards:
            try:
                title = card.find("h2", class_="title").text.strip()
                company = card.find("h3", class_="company").text.strip()
                location = card.find("p", class_="location").text.strip()
                date_posted = card.find("time").text.strip()

                
                salary = random.randint(50000, 150000)
                exp_level = random.choice(experience_levels)
                work_mode = random.choice(work_modes)

                self.jobs_data.append({
                    "Job Title": title,
                    "Company Name": company,
                    "Location": location,
                    "Salary": salary,
                    "Experience Level": exp_level,
                    "Work Mode": work_mode,
                    "Date Posted": date_posted
                })
            except Exception as e:
                continue

    def save_to_csv(self):
        df = pd.DataFrame(self.jobs_data)
        
        df.to_csv("raw_jobs_dataset.csv", index=False)
        print("Success!.")

if __name__ == "__main__":
    url = "https://realpython.github.io/fake-jobs/"
    scraper = JobScraper(url)
    html = scraper.fetch_page()
    scraper.parse_jobs(html)
    scraper.save_to_csv()