import pandas as pd

class SkillMatcher:
    def __init__(self, market_skills, user_skills_file):
        self.market_skills = [skill.strip().lower() for skill in market_skills.index]
        self.user_skills_file = user_skills_file
        self.user_skills = []

    def load_user_skills(self):
        df = pd.read_csv(self.user_skills_file)
        self.user_skills = df["skills"].str.lower().tolist()

    def get_matching_skills(self):
        return list(set(self.user_skills).intersection(set(self.market_skills)))

    def get_missing_skills(self):
        return list(set(self.market_skills) - set(self.user_skills))