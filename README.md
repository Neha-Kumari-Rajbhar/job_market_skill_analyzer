
# 📊 Job Market Skill Analyzer
## 📌 Overview

The **Job Market Skill Analyzer** is a Python-based application that analyzes job market data to identify in-demand skills and compares them with a user’s existing skills.
It helps users understand **skill gaps** and focus on the most required skills in the job market.

This project uses **Pandas** and **NumPy** for data processing and analysis, and generates an automated text report.
## 🚀 Features

✔ Reads job market data from a CSV file (`jobs.csv`)
✔ Cleans and processes data using **Pandas**
✔ Identifies:

* Most demanded skills
* Top job locations

✔ Reads user skills from a text file (`my_skills.txt`)
✔ Compares:

* User skills vs job market skills

✔ Generates a report showing:

* Top demanded skills
* Matching skills
* Missing skills
* Top job locations

✔ Uses **Object-Oriented Programming (OOP)**
✔ Uses **file handling** for input and output
✔ Modular code structure (multiple Python files)

## Tech Stack

* Python
* Pandas
* NumPy
* File Handling
* Object-Oriented Programming (OOP)

## 📂 Project Structure

```
Job-Market-Skill-Analyzer/
│
├── jobs.csv
├── my_skills.txt
├── analyzer.py
├── report_generator.py
├── main.py
├── output_report.txt
└── README.md
```

## How It Works

1. The program reads job data from `jobs.csv`.
2. It cleans and processes the dataset using Pandas.
3. It extracts:

   * Most demanded skills
   * Top job locations
4. It reads user skills from `my_skills.txt`.
5. It compares user skills with job market skills.
6. It generates a text report (`output_report.txt`) with:

   * Top skills
   * Matching skills
   * Missing skills
   * Top locations

## ▶️ How to Run

1. Clone the repository:

```
git clone <your-repo-link>
```

2. Install required libraries:

```
pip install pandas numpy
```

3. Run the project:

```
python main.py
```

4. Check the generated report:

```
output_report.txt
```

## 📄 Sample Output (Report)

```
Top Demanded Skills: Python, SQL, Excel, Machine Learning  
Matching Skills: Python, SQL  
Missing Skills: Machine Learning, Excel  
Top Job Locations: Bangalore, Hyderabad, Pune
```

## 🎯 Learning Outcomes

* Data cleaning and analysis using Pandas
* Skill gap analysis logic
* File handling in Python
* Applying OOP concepts
* Writing modular and maintainable code
* Real-world job market data analysis

## 👩‍💻 Author

**Neha Kumari Rajbhar**

* GitHub: [https://github.com/Neha-Kumari-Rajbhar](https://github.com/Neha-Kumari-Rajbhar)
* LinkedIn: [https://www.linkedin.com/in/neha-kumari-rajbhar](https://www.linkedin.com/in/neha-kumari-rajbhar)
