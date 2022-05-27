import inspect


def smartprint(*argv):
    """
    The string representation of the argument is
    concatenated to its value
    """
    line_of_code = inspect.getframeinfo(inspect.stack()[1][0]).code_context[0].strip()
    opening_bracket_location = line_of_code.find("(") + 1
    closing_bracket_location = line_of_code.rfind(")")

    print(line_of_code[opening_bracket_location:closing_bracket_location], ":", *argv)
