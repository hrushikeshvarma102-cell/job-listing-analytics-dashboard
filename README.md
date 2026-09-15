# 📊 Job Listing Analytics Dashboard

A Python-based **Job Listing Analytics Dashboard** that collects, cleans, processes, analyzes, and visualizes job listing data through an interactive **Streamlit dashboard**.

---

## 🚀 Project Overview

The **Job Listing Analytics Dashboard** is a data analytics project designed to understand job market data and generate useful insights from job listings.

The project follows a complete data pipeline:

```text
Job Listing Website
        ↓
Web Scraping
        ↓
Raw Job Dataset
        ↓
Data Cleaning
        ↓
Data Processing
        ↓
Data Analysis
        ↓
Streamlit Dashboard


The dashboard provides insights into:

💼 Job openings
💰 Compensation / salary
🏢 Companies
🎯 Experience levels
🏠 Work modes
📈 Salary trends
📊 Job listing statistics
✨ Features
🕷️ Web Scraping
Collects job listing information.
Extracts relevant job-related fields.
Stores scraped data in CSV format.
🧹 Data Cleaning
Handles missing values.
Removes duplicate records.
Cleans inconsistent data.
Converts columns into appropriate data types.
⚙️ Data Processing
Processes compensation/salary information.
Processes experience levels.
Processes work modes.
Creates salary categories.
Prepares datasets for analysis.
📊 Interactive Dashboard

The Streamlit dashboard provides:

Total job openings
Average compensation
Company analysis
Experience-level analysis
Work-mode analysis
Salary analysis
Salary categories
Seniority vs. salary analysis
Filtered job database
🎛️ Interactive Filters

Users can filter the dashboard based on:

Work Mode
Experience Level
🛠️ Technologies Used
Technology	Purpose
🐍 Python	Core programming
🐼 Pandas	Data cleaning and analysis
🌐 Requests	HTTP requests
🍲 BeautifulSoup	Web scraping
📊 Streamlit	Interactive dashboard
📄 CSV	Dataset storage



job-listing-analytics-dashboard/
│
├── app.py
│
├── scrape_jobs.py
│
├── process_and_analyze.py
│
├── raw_jobs_dataset.csv
│
├── cleaned_jobs_dataset.csv
│
├── processed_jobs_dataset.csv
│
├── requirements.txt
│
├── README.md
│
└── .gitignore



1️⃣ Web Scraping

The scrape_jobs.py script collects job listing data.

Job Listing Website
        ↓
scrape_jobs.py
        ↓
raw_jobs_dataset.csv

Run:

python scrape_jobs.py





2️⃣ Data Cleaning & Processing

The process_and_analyze.py script cleans and processes the scraped dataset.

raw_jobs_dataset.csv
        ↓
Data Cleaning
        ↓
Data Processing
        ↓
cleaned_jobs_dataset.csv
        ↓
processed_jobs_dataset.csv

Run:

python process_and_analyze.py



3️⃣ Dashboard

The app.py file loads the processed dataset and creates the Streamlit dashboard.

processed_jobs_dataset.csv
        ↓
app.py
        ↓
Streamlit Dashboard

Run:

streamlit run app.py




💻 Installation Guide

Follow the steps below to run this project on your computer.

1️⃣ Clone the Repository

Open PowerShell / CMD / Terminal and run:

git clone https://github.com/hrushikeshvarma102-cell/job-listing-analytics-dashboard.git
2️⃣ Navigate to the Project Folder
cd job-listing-analytics-dashboard

Check the files:

PowerShell
dir
CMD
dir

You should see files such as:

app.py
scrape_jobs.py
process_and_analyze.py
requirements.txt
README.md



🐍 Python Virtual Environment

Creating a virtual environment is recommended so that project dependencies stay isolated.

3️⃣ Create Virtual Environment

Windows:

python -m venv venv

This creates:venv/



4️⃣ Activate Virtual Environment
PowerShell
venv\Scripts\Activate.ps1
CMD
venv\Scripts\activate

After activation, you should see something similar to:

(venv) PS C:\...\job-listing-analytics-dashboard>


5️⃣ Upgrade pip
python -m pip install --upgrade pip
📦 Install Dependencies

6️⃣ Install Required Packages

The project dependencies are stored in requirements.txt.

Run:

pip install -r requirements.txt

The main packages include:

streamlit
pandas
requests
beautifulsoup4


🕷️ Run Web Scraper

After installing the dependencies, run:

python scrape_jobs.py

The scraper collects the job listing data.

The raw dataset is saved as:

raw_jobs_dataset.csv

🧹 Process the Dataset

After scraping the data, run:

python process_and_analyze.py

This performs data cleaning and processing.

The resulting files are:

cleaned_jobs_dataset.csv
processed_jobs_dataset.csv

📊 Run Streamlit Dashboard

Start the dashboard:

streamlit run app.py

Streamlit will start a local server.

You can normally access the application through:

http://localhost:8501



