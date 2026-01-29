import pandas as pd

class JobAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        return self.df

    def clean_data(self):
        self.df = self.df.copy()
        self.df["skills"] = self.df["skills"].str.lower()
        return self.df

    def get_top_skills(self, n=10):
        all_skills = self.df["skills"].str.split(",").explode()
        return all_skills.value_counts().head(n)

    def get_top_locations(self, n=5):
        return self.df["location"].value_counts().head(n)