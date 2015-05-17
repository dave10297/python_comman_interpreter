from custom_exceptions import *

# Tries to convert the string to an int if ValueError was raised, then either it's a float
def ConvertArgumentToNumber(string_number):
    try: # attempt at converting to an integer
        number = int(string_number)
    except ValueError:
        try: # attempt at converting to a float
            number = float(string_number)
        except ValueError: # could not convert to an integer or a float, must be a word
            print "Error: argument '{0}' could not be converted to a number".format(string_number)
            raise ArgumentConvertError
            return

    return number
