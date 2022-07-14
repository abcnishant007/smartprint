import unittest
import sys
import numpy as np
import io
import os
import sys

from src.smartprint.__init__ import smartprint as sprint


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

    def test_any_keyword_name_import(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        np.random.seed(0)
        from src.smartprint.__init__ import smartprint as random_name

        random_name(np.random.rand())

        assert redir_to_var.getvalue().strip() == "np.random.rand() : 0.5488135039273248"

        sys.stdout = old_stdout

    def test_keyword_arguments(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        np.random.seed(0)
        from src.smartprint.__init__ import smartprint as random_name

        random_name(np.random.rand())

        assert redir_to_var.getvalue().strip() == "np.random.rand() : 0.5488135039273248"

        sys.stdout = old_stdout

    def test_dict_prettyprint(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        sprint(dict(zip(list(range(8, 5, -1)), list(range(4, 1, -1)))))

        assert (
            redir_to_var.getvalue().strip()
            == "Dict: dict(zip(list(range(8, 5, -1)), list(range(4, 1, -1))))\nKey: Value\n{6: 2, 7: 3, 8: 4}"
        )

        sys.stdout = old_stdout

    def test_list_prettyprint(self):
        redir_to_var = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = redir_to_var

        # actual call
        myList = [1, 4, -5, "Nishant"]
        sprint(myList)

        assert redir_to_var.getvalue().strip() == "List: myList\n[1, 4, -5, 'Nishant']"

        sys.stdout = old_stdout
