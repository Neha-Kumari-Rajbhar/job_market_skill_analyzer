import pandas as pd

# Load the CSV files
postings = pd.read_csv("data/job_postings.csv")
skills = pd.read_csv("data/job_skills.csv")

# Select only useful columns
postings = postings[["job_link", "job_title", "job_location"]]
skills = skills[["job_link", "job_skills"]]

# Merge both files using job_link
merged = pd.merge(postings, skills, on="job_link", how="inner")

# Rename columns to match our project format
final_df = merged.rename(columns={
    "job_skills": "skills",
    "job_location": "location"
})

# Keep only required columns
final_df = final_df[["job_title", "skills", "location"]]

# Save new dataset
final_df.to_csv("data/jobs.csv", index=False)

#print("jobs.csv created successfully!")