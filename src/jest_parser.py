import json
import re


def clean(message) :
    message = bytes(message, "utf-8").decode("unicode_escape")
    message = re.sub(r'\s*\(/.*?\)', '', message)
    message = re.sub(r'\x1b\[[0-9;]*m', '', message)
    message = message.replace('\n\n', '\n').strip()

    return message


def parse_jest_results(file_path):
    with open("./sample.json", 'r') as f:
        results = json.load(f)

    failed_tests = []

    for i, test in enumerate(results['testResults']) :
        
        if(i == 1) :
            break

        for assertion in test['assertionResults']:
            if assertion['status'] == 'failed':
                failure_message = '\n'.join(assertion['failureMessages'])

                expected_match = re.search(r'Expected[\s\S]*?(?=\n\n|$)', failure_message)
                additional_errors = re.sub(r'Expected[\s\S]*?(?=\n\n|$)', '', failure_message).strip()
                failed_test = {
                    'name': assertion['title'],
                    'reason': clean(expected_match.group(0)) if expected_match else "No expected value found."
                }

                if additional_errors:
                    failed_test['reason'] += '\n' + clean(additional_errors)

                failed_tests.append(failed_test)

    print(json.dumps({'failedTests': failed_tests}, indent=2))

if __name__ == "__main__" :
    parse_jest_results('jest-test-results.json')
