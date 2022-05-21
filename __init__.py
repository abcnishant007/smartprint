import inspect

def smartprint(arg):
    """
    The string representation of the argument is
    concatenated to its value
    """
    try:
        dictitems = inspect.currentframe().f_back.f_locals.items()
        prev_name = [prev_name for prev_name, prev_val in dictitems if prev_val is arg][0]
        print (prev_name, ":" , arg)
    except:
        print (arg)
