# generate_grade.py

import sys
import os
import xml.etree.ElementTree as ET
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


# Parse the JUnit XML file and return the test results


def parse_junit_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    status_string = ""
    tests = 0
    failures = 0
    errors = 0
    skipped = 0

    for testsuite in root.findall('testsuite'):

        # Add up the test results from each testsuite

        tests += int(testsuite.attrib.get('tests', 0))
        failures += int(testsuite.attrib.get('failures', 0))
        errors += int(testsuite.attrib.get('errors', 0))
        skipped += int(testsuite.attrib.get('skipped', 0))

        # Add a character to the status string for each testcase

        for testcase in testsuite.findall('testcase'):
            if any(child.tag == "failure" for child in testcase):
                status_string += "F"
            elif any(child.tag == "error" for child in testcase):
                status_string += "E"
            elif any(child.tag == "skipped" for child in testcase):
                status_string += "S"
            else:
                status_string += "."

    passed = tests - failures - errors - skipped

    return tests, passed, failures, errors, skipped, status_string


def generate_grade(tests, passed):
    grade = (passed / tests) if tests > 0 else 0
    return grade


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python grade.py <xml-results-file>")
        sys.exit(1)

    results_file = sys.argv[1]

    tests, passed, failures, errors, skipped, status_string = parse_junit_xml(results_file)
    grade = generate_grade(tests, passed)
    # print(f"Total Tests: {tests}")
    # print(f"Passed Tests: {passed}")
    # print(f"Failed Tests: {failures}")
    # print(f"Errors: {errors}")
    # print(f"Skipped: {skipped}")
    print(f"{grade:.2f}", ",", status_string)
