import unittest2
from tests.test_login_to_petstore import TestLoginToPetstore
import HtmlTestRunner


def create_test_suite():
    loader = unittest2.TestLoader()
    suite = unittest2.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLoginToPetstore))
    return suite


if __name__ == "__main__":
    test_suite = create_test_suite()
    runner = unittest2.TextTestRunner()

    # Specify the path to save the HTML report
    report_path = "C:/Users/locke/PycharmProjects/selenium-petstore/testreport"

    # Create a test runner with HtmlTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(
        output=report_path,
        report_title="Test Report",
    )

    # Run the test suite and generate the HTML report
    result = runner.run(test_suite)
