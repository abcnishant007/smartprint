import inspect
from pprint import pprint


def smartprint(*argv, **kwargs):
    """
    The string representation of the argument is
    concatenated to its value
    """

    line_of_code = inspect.getframeinfo(inspect.stack()[1][0]).code_context[0].strip()
    opening_bracket_location = line_of_code.find("(") + 1
    closing_bracket_location = line_of_code.rfind(")")
    extracted_code = line_of_code[opening_bracket_location:closing_bracket_location]

    # additional test to make sure extra brackets do not wreck our code
    extracted_code = extracted_code.replace("sprint", "").replace("prints", "").\
                            replace("smartprint","").replace("print","")

    if len(argv) == 1 and len(kwargs) == 0:
        if isinstance(argv[0], list):
            helper_smartprint_list(argv[0], extracted_code)
        elif isinstance(argv[0], dict):
            helper_smartprint_dict(argv[0], extracted_code)
        else:
            print(extracted_code, ":", *argv, **kwargs)
    else:
        print(extracted_code, ":", *argv, **kwargs)


def helper_smartprint_list(l, extracted_code):
    print("List:", extracted_code)
    pprint(l)


def helper_smartprint_dict(d, extracted_code):
    print("Dict:", extracted_code)
    print("Key: Value")
    pprint(d)
