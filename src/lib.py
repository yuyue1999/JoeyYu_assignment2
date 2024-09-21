import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
# from fpdf import FPDF

def read_dataset(path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(script_dir, path)
    df = pd.read_csv(dataset_path)
    return df


def statistics(df):
    print(df.describe())
#
# def generate_pdf(df, pdf_path="../AI-Powered_Job_Report.pdf"):
#     pdf = FPDF()
#     mean_salary, median_salary, std_salary = (
#         df["Salary_USD"].mean(),
#         df["Salary_USD"].median(),
#         df["Salary_USD"].std(),
#     )
#
#     min_salary, percentile_25_salary, percentile_75_salary, max_salary = (
#         df["Salary_USD"].min(),
#         df["Salary_USD"].quantile(0.25),
#         df["Salary_USD"].quantile(0.75),
#         df["Salary_USD"].max(),
#     )
#
#     pdf.add_page()
#
#     pdf.set_font("Arial", "B", 16)
#     pdf.cell(200, 10, txt="AI Powered Job Report", ln=True, align="C")
#
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(
#         200,
#         10,
#         txt="Descriptive Statistics for Salary(mean, median, std), Company Size and Required Skills",
#         ln=True,
#         align="L",
#     )
#
#     pdf.cell(200, 10, txt=f"Mean Points: {mean_salary:.2f}", ln=True)
#     pdf.cell(200, 10, txt=f"Median Points: {median_salary:.2f}", ln=True)
#     pdf.cell(200, 10, txt=f"Standard Deviation of Points: {std_salary:.2f}", ln=True)
#
#     pdf.cell(200, 10, txt=f"Min Salary: {min_salary:.2f}", ln=True)
#     pdf.cell(200, 10, txt=f"Percentile 25 Salary: {percentile_25_salary:.2f}", ln=True)
#     pdf.cell(200, 10, txt=f"Percentile 75 Salary: {percentile_75_salary:.2f}", ln=True)
#
#     pdf.cell(200, 10, txt=f"Max Salary: {max_salary:.2f}", ln=True)
#
#
#     pdf.cell(200, 10, txt="Distribution of Company Sizes", ln=True)
#     pdf.image("../companysize_histogram.png", x=10, y=70, w=190)
#
#     pdf.add_page()
#     pdf.cell(200, 10, txt="Job Growth Projection", ln=True)
#     pdf.image("../jobgrowth_histogram.png", x=10, y=70, w=190)
#
#     pdf.add_page()
#     pdf.cell(200, 10, txt="Top 20 Most Frequent Required Skills", ln=True)
#     pdf.image("../requiredskill_histogram.png", x=10, y=70, w=190)
#
#     pdf.output(pdf_path)

def companysize(df):

    company_size_stats = df['Company_Size'].describe()
    print(company_size_stats)


    company_size_counts = df['Company_Size'].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(company_size_counts, labels=company_size_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Company Sizes')
    plt.savefig("../companysize_histogram.png")
    plt.show()

def jobgrowth(df):
    job_growth_stats = df['Job_Growth_Projection'].describe()
    print(job_growth_stats)


    plt.figure(figsize=(10, 6))
    plt.hist(df['Job_Growth_Projection'].dropna(), bins=20, color='blue', alpha=0.7)
    plt.title('Histogram of Job Growth Projections')
    plt.xlabel('Job Growth Projection')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig("../jobgrowth_histogram.png")
    plt.show()

def requiredskill(df):
    skills_series = df['Required_Skills'].dropna().apply(lambda x: x.split(','))
    all_skills = [skill.strip() for sublist in skills_series for skill in sublist]

    skill_counts = Counter(all_skills)

    skill_df = pd.DataFrame(skill_counts.items(), columns=['Skill', 'Count']).sort_values(by='Count', ascending=False)


    plt.figure(figsize=(14, 8))
    plt.bar(skill_df['Skill'][:20], skill_df['Count'][:20], color='green')
    plt.xlabel('Skills')
    plt.ylabel('Frequency')
    plt.title('Top 20 Most Frequent Required Skills')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("../requiredskill_histogram.png")
    plt.show()


def main():
    dataset_path = "../ai_job_market_insights.csv"
    df = read_dataset(dataset_path)
    statistics(df)
    companysize(df)
    jobgrowth(df)
    requiredskill(df)
    # generate_pdf(df)


if __name__ == "__main__":
    main()