import unittest

# Importing tests
import main


def run_suite(   module):
    suite = unittest.TestLoader().loadTestsFromModule(module)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    for module in [main]:
        run_suite(module)
