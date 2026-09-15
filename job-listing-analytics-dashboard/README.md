# Job Listing Analytics Dashboard

A Streamlit-based job market analytics dashboard that processes job listings and presents insights about salaries, experience levels, work modes, companies, and job records.

## Features

- Scrapes job listings from the Real Python fake jobs website
- Cleans and processes the collected dataset
- Removes duplicate and missing records
- Converts salary values to numeric format
- Creates salary categories: Low, Medium, and High
- Interactive Streamlit dashboard
- Filter jobs by:
  - Work Mode
  - Experience Level
- Executive overview with:
  - Active openings
  - Average compensation
  - Number of participating companies
- Salary analysis by work mode
- Seniority vs. salary analysis
- Filtered job database view

## Tech Stack

- Python
- Streamlit
- Pandas
- Requests
- BeautifulSoup

## Project Structure

```text
JOB LISTING ANALYTICS DASHBOARD/
│
├── app.py
├── scrape_jobs.py
├── process_and_analyze.py
│
├── raw_jobs_dataset.csv
├── cleaned_jobs_dataset.csv
├── processed_jobs_dataset.csv
│
├── .gitignore
└── README.md
```

## How the Project Works

```text
Job Website
    ↓
scrape_jobs.py
    ↓
raw_jobs_dataset.csv
    ↓
process_and_analyze.py
    ↓
cleaned_jobs_dataset.csv
    ↓
processed_jobs_dataset.csv
    ↓
app.py
    ↓
Streamlit Analytics Dashboard
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

Create and activate a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install streamlit pandas requests beautifulsoup4
```

## Run the Project

If you already have the processed dataset:

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## Generate the Dataset Again

To scrape fresh job listings:

```bash
python scrape_jobs.py
```

Then clean and process the data:

```bash
python process_and_analyze.py
```

Finally start the dashboard:

```bash
streamlit run app.py
```

## Important Note

The project uses the Real Python **fake jobs** website as the scraping source for demonstration and learning purposes.

Salary, experience level, and work mode values in the scraper are generated for the demo dataset rather than representing verified real-world compensation data.

## GitHub Upload

Recommended GitHub repository name:

`job-listing-analytics-dashboard`

Before uploading, do **not** commit your local `venv/` folder. The included `.gitignore` prevents it from being uploaded.

## Future Improvements

- Add more job websites/APIs
- Add salary distribution charts
- Add location-based analytics
- Add keyword and job-title search
- Add export/download functionality
- Add database storage
- Deploy the Streamlit dashboard online
- Add automated scheduled data collection

## Author

**Hrushikesh Varma**

GitHub: https://github.com/hrushikeshvarma102-cell
