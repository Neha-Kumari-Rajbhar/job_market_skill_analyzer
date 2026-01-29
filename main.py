from analyser import JobAnalyzer
from skill_match import SkillMatcher
from report_generator import ReportGenerator

DATA_FILE = "data/jobs.csv"
USER_SKILLS_FILE = "data/my_skills.txt"

def main():
    analyzer = JobAnalyzer(DATA_FILE)

    # Day 1: Data Analysis
    df = analyzer.load_data()
    df = analyzer.clean_data()

    top_skills = analyzer.get_top_skills()
    top_locations = analyzer.get_top_locations()

    print("Top Skills:")
    print(top_skills)
    print("Salary data not available in dataset")
    print("Top Locations:")
    print(top_locations)

    # Day 2: Skill Matching
    matcher = SkillMatcher(top_skills, USER_SKILLS_FILE)
    matcher.load_user_skills()

    matching_skills = matcher.get_matching_skills()
    missing_skills = matcher.get_missing_skills()

    print("Matching Skills:", matching_skills)
    print("Missing Skills:", missing_skills)

    # Generate Report
    report = ReportGenerator()
    report.generate_report(top_skills, top_locations, matching_skills, missing_skills)

    print("\nReport generated successfully as report.txt")

if __name__ == "__main__":
    main()