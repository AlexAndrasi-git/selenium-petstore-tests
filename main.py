import unittest
import os
from tests.test_login_to_petstore import TestLoginToPetstore
from tests.test_verify_find_pet_functions import TestVerifyFindPetFunctions
import HtmlTestRunner


def create_test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLoginToPetstore))
    suite.addTests(loader.loadTestsFromTestCase(TestVerifyFindPetFunctions))
    return suite


if __name__ == "__main__":
    test_suite = create_test_suite()
    runner = unittest.TextTestRunner()

    # Specify the path to save the HTML report
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        report_path = "/home/runner/work/selenium-petstore/selenium-petstore/testreport"
    else:
        report_path = "testreport"

    # Create a test runner with HtmlTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        output=report_path,
        report_title="Test Report",
    )

    # Run the test suite and generate the HTML report
    result = runner.run(test_suite)
