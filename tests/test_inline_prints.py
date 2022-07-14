import unittest
import sys
import numpy as np
import io

from __init__ import smartprint as sprint


class SmartPrintTestsInLinePrints(unittest.TestCase):
    def test_inline_print_different_line_output(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        a = [1, 2, 3]
        for k in a:
            sprint(k)

        assert redir_to_var.getvalue().strip() == "k : 1\nk : 2\nk : 3"

        sys.stdout = old_stdout

    def test_inline_print_single_line(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        a = [1, 2, 3]
        for k in a: sprint(k)

        assert redir_to_var.getvalue().strip() == "k : 1\nk : 2\nk : 3"

        sys.stdout = old_stdout


    def test_inline_print_more_brackets(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        a = [1, 2, 3]
        for k in a: (sprint(k))

        assert redir_to_var.getvalue().strip() == "(k) : 1\n(k) : 2\n(k) : 3"

        sys.stdout = old_stdout
