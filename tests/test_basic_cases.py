import unittest
import sys
sys.path.append("../")
import numpy as np
import io
from __init__ import smartprint as sprint


class SmartPrintTests(unittest.TestCase):
    def test_numeric_value(self):
        old_stdout = sys.stdout

        redir_to_var = io.StringIO()
        sys.stdout = redir_to_var

        # actual call
        a = 25
        sprint(a)

        assert redir_to_var.getvalue().strip() == "a : 25"

        sys.stdout = old_stdout

    def test_other_objects(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        np.random.seed(0)
        sprint(np.random.rand())

        assert redir_to_var.getvalue().strip() == "np.random.rand() : 0.5488135039273248"

        sys.stdout = old_stdout


# if __name__ == "__main__":
#     SmartPrintTests.test_numeric_value()
#     SmartPrintTests.test_other_objects()
#     # SmartPrintTests.test_other_objects()
