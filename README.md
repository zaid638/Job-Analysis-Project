# Job-Analysis-Project
<br />

Analyze job postings to identify trends and insights in job requirements.
<br /><br />

## Objective
<br />

* The main goal of this project is to analyze job postings to identify trends and insights in job requirements, such as in-demand skills, education levels, and experience.
<br />

* This analysis will help job seekers and recruiters understand the current job market.
<br /><br /><br />

## Scope
<br />

**Data Source:** Job postings were collected from (http://www.topjobs.lk) using a Python web scraping script (Beautiful Soup). This analysis include data from June to September 2024.
<br /><br />

**Key Data Fields:**   Job Title, Company, Skills, Education, Experience, and Job Links.
<br /><br />

**Time Frame:**   The data was scraped weekly to capture recent trends.
<br /><br />

**Tools Used:**   Python (scraping and cleaning), Excel (data storing and organization), PowerBI (dashboarding).
<br /><br /><br />

## Approach
<br />

**Data Collection**
<br />

  - Scraped job postings weekly.
  - Extracted key fields: Job Title, Company, Job Link.
<br />

**Data Cleaning and Transformation**
<br />

  - Filtered only relevant job postings using Python (data analyst, data engineer, data scientist, python, cloud, cyber security).
  - Manually inserted and populated additional columns such as Skills, Education, Experience using data from job-specific links.
<br />

**Dashboard Creation**
<br />

  - Built an interactive dashboard in PowerBI to visualize key metrics such as in-demand skills, required experience, and education levels.
<br /><br /><br />

## Current Status
<br />

- **Data Collection:** Job data is successfully being collected and added weekly.
<br />

- **Data Cleaning:**  Completed after every data collection, ensuring only relevant data is used.
<br />

- **Dashboard:** An operational PowerBI dashboard visualizes trends and insights.
<br /><br /><br />

## Future Expansion
<br />

**1. Automating the Process**
  - Fully automate data scraping, cleaning, and transformation tasks to reduce manual input.
<br />

**2. Prediction Model**
  - Build a predictive model to forecast future job trends and in-demand skills based on the current data.
<br />

**3. System Deployment**
  - Deploy this job analysis system on a website.
  - Integrate GenAI (LLM) to provide job seekers with personalized job recommendations and insights.
<br /><br /><br />

## Dashboard
<br />

![Dashboard](https://github.com/zaid638/Job-Analysis-Project/blob/main/Dashboard.png)
<br /><br /><br />

## Data Insights (from June to September 2024)
<br />

**1. Job Titles**
  - There are 140 jobs  in the dataset.
  - The most jobs are related to Information Security.
  - Trend of job counts are fluctuating.
<br />

**2. Companies**
  - A total of 86 unique companies are represented in the job postings.
  - The most companies are hiring jobs related to Data Analyst.
<br />

**3. Education Levels**
  - The majority of job postings require a Bachelor’s degree.
  - Most of the entry level jobs are not required a higher education levels and some of them are required Diploma or HND (Higher National Diploma).
  - Some senior level job positions are required to have Master’s degree.
  - Data Engineering jobs required least percentage of education (63%).
<br />

**4. Experience**
  - Most of the entry-level jobs require no experience.
  - Least average experience require for Data Analyst (1.3 years) and Data Scientist (1.2 years) while Most Average experience require for Machine Learning Engineer Position (4.3 years).
  - The lead and senior level job positions are required highest experience like 5 to 9 years.
<br />

**5. Skills**
<br />

* Communication is most relevant skill for every job.
* Python
  - Expertise in Python language
  - Working with APIs
  - Flask and Django
  - Cloud Technologies
<br />

* Data Analyst
  - Python, SQL, Excel, PowerBI
<br />

* Data Scientist
  - Python, SQL, Statistics
  - Data Analysis, Machine Learning
<br />

* Data Engineer
  - Python, SQL
  - ETL / ELT , Pipeline Building
  - Database, Cloud Technologies, Data Warehouse

* Machine Learning Engineer
  - Python, APIs
  - Cloud Technologies
<br />

* Cloud Engineer
  - Cloud Technologies (Azure, AWS)
  - DevOps, Containers, CI/CD
  - Databases, Linux
<br />

* Information Security / Cyber Security
  - Certifications (CISSP, CEH)
  - Networking, Cloud Technologies, VAPTs, Operating Systems
<br /><br /><br />

## Recommendations
<br />

### For Job Seekers
<br />

* Focus on Communication as it is the most sought-after skill.
* If you're entering the Data field, proficiency in Python, SQL and ETL will make you more competitive.
* Most job postings prefer candidates with a Bachelor's degree, so it's worth completing this level of education if possible.
<br />

### For Companies
<br />

* Companies should consider offering training in top-demand skills like Communication, Python, and SQL to bridge any skill gaps in their current workforce.
* Since many jobs are open to entry-level candidates (0-2 years of experience), companies might benefit from providing internships and training programs to attract fresh talent.
<br /><br /><br />

## Conclusion
<br />

* The project has successfully collected, cleaned, and analyzed job posting data to provide insights into the job market.
* Future improvements will focus on automating data collection, building predictive capabilities, and enhancing accessibility via a web interface with AI integration.
<br /><br /><br />




