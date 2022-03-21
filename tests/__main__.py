import unittest

# Importing tests
import main_test


def run_suite(module):
    suite = unittest.TestLoader().loadTestsFromModule(module)
    unittest.TextTestRunner(verbosity=2).run(suite)


for module in [main_test]:
    run_suite(module)
