import os

from utils.file import join_paths

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = join_paths([SRC_DIR, "..", "tests"])

