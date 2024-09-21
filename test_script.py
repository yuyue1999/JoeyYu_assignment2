from test_lib import (
    test_stat,
    test_hist_companysize,
    test_hist_jobgrowth,
    test_hist_requiredskill,
)


def run_tests():
    test_stat()
    test_hist_companysize()
    test_hist_jobgrowth()
    test_hist_requiredskill()
    # test_pdf_gen()

    print("All tests completed successfully!")


if __name__ == "__main__":
    run_tests()
