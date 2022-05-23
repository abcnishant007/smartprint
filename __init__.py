import inspect


def smartprint(*argv, **kwargs):
    """
    The string representation of the argument is
    concatenated to its value
    """
    try:
        line_of_code = inspect.getframeinfo(inspect.stack()[1][0]).code_context[0]
        message = line_of_code.replace("smartprint", "").replace("sprint", "").strip()[1:-1]
        print(message, ":", *argv, **kwargs)
    except:
        print(*argv, **kwargs)
