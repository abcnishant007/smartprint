import inspect


def smartprint(*argv):
    """
    The string representation of the argument is
    concatenated to its value
    """
    line_of_code = inspect.getframeinfo(inspect.stack()[1][0]).code_context[0]
    var_names = line_of_code.replace("smartprint", "").replace("sprint", "").strip()[1:-1]
    print(var_names, ":", *argv)
