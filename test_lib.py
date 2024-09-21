import os
from src.lib import statistics, companysize, read_dataset, jobgrowth, requiredskill

dataset_path = "../ai_job_market_insights.csv"
df = read_dataset(dataset_path)


def _file_exists_and_not_empty(filepath):
    return os.path.exists(filepath) and os.path.getsize(filepath) > 0


def test_stat():
    statistics(df)


def test_hist_companysize():
    try:
        companysize(df)
        flag = True
    except Exception as e:
        flag = False
    assert flag
    assert _file_exists_and_not_empty("companysize_histogram.png")

def test_hist_jobgrowth():
    try:
        jobgrowth(df)
        flag = True
    except Exception as e:
        flag = False
    assert flag
    assert _file_exists_and_not_empty("jobgrowth_histogram.png")

def test_hist_requiredskill():
    try:
        requiredskill(df)
        flag = True
    except Exception as e:
        flag = False
    assert flag
    assert _file_exists_and_not_empty("requiredskill_histogram.png")

#
# def test_pdf_gen():
#     generate_pdf(df)
#     assert _file_exists_and_not_empty("../AI-Powered_Job_Report.pdf")