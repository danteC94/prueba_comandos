import unittest
from test_principal import TestPrincipal


def suite():
    test_suite = unittest.test_suite()
    test_suite.addTest(unittest.makeSuite(TestPrincipal))
    return test_suite


if __name__ == "__main__":
    unittest.main()
