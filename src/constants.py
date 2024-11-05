import os

from utils.file import join_paths

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = join_paths([SRC_DIR, "..", "tests"])

TEST_APP_DIR = join_paths([SRC_DIR, "..", "test-app"])
TEST_APP_SRC_DIR = join_paths([TEST_APP_DIR, "src"])
TEST_APP_COMPONENTS_DIR = join_paths([TEST_APP_SRC_DIR, "components"])

JEST_TEST_RESULTS_PATH = join_paths([TEST_APP_SRC_DIR, "jest-test-results.json"])
