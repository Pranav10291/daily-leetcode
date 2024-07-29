import unittest
import sys
import os

if __name__ == '__main__':
    # Add the project root directory to the Python path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    # Discover and run all tests
    test_suite = unittest.defaultTestLoader.discover('tests')
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    # Exit with a non-zero code if there were failures
    sys.exit(not result.wasSuccessful())