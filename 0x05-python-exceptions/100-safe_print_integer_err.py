#!/usr/bin/python3
# Task 7

def safe_print_integer_err(value):
    """
    A function that prints an integer and returns
    True if value has.
    been correctly printed (it means the value is an integer)
    Otherwise, returns False.
    and prints in stderr the error precede by Exception
    """
     try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
