import unittest2
import os
from tests.test_login_to_petstore import TestLoginToPetstore
from tests.test_verify_pet_view_functions import TestVerifyPetViewFunctions
import HtmlTestRunner


def create_test_suite():
    loader = unittest2.TestLoader()
    suite = unittest2.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLoginToPetstore))
    suite.addTests(loader.loadTestsFromTestCase(TestVerifyPetViewFunctions))
    return suite


if __name__ == "__main__":
    test_suite = create_test_suite()
    runner = unittest2.TextTestRunner()

    # Specify the path to save the HTML report
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        report_path = "/home/runner/work/selenium-petstore/selenium-petstore/testreport"
    else:
        report_path = "C:/Users/locke/PycharmProjects/selenium-petstore/testreport"

    # Create a test runner with HtmlTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        output=report_path,
        report_title="Test Report",
    )

    # Run the test suite and generate the HTML report
    result = runner.run(test_suite)
