class ReportGenerator:
    def generate_report(self, top_skills, top_locations, matching_skills, missing_skills):
        with open("report.txt", "w") as f:
            f.write("JOB MARKET SKILL ANALYSIS REPORT\n")
            f.write("=" * 40 + "\n\n")

            f.write("Top Skills in Market:\n")
            for skill, count in top_skills.items():
                f.write(f"{skill}: {count}\n")

            f.write("\nTop Job Locations:\n")
            for loc, count in top_locations.items():
                f.write(f"{loc}: {count}\n")

            f.write("\nYour Matching Skills:\n")
            for skill in matching_skills:
                f.write(f"{skill}\n")

            f.write("\nSkills You Should Learn:\n")
            for skill in missing_skills[:10]:
                f.write(f"{skill}\n")