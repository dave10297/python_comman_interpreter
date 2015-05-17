from utilities import *
from subprocess import call #to invoke the shell command 'clear'

# Command Implementations
def HelloCommand(args):
    print "Hello and welcome to this little command interpreter developed and programmed by David Burns!"

def ExitCommand(args):
    pass

def ClearCommand(args):
    call("clear")

def AddCommand(args):
    try:
        result = ConvertArgumentToNumber(args[0])
        for argument in args[1 : ]:
            result = result + ConvertArgumentToNumber(argument)
    except ArgumentConvertError:
        return

    print result

def SubCommand(args):
    try:
        result = ConvertArgumentToNumber(args[0])
        for argument in args[1 : ]:
            result = result - ConvertArgumentToNumber(argument)
    except ArgumentConvertError:
        return

    print result

def MultCommand(args):
    try:
        result = ConvertArgumentToNumber(args[0])
        for argument in args:
            result = result * ConvertArgumentToNumber(argument)
    except ArgumentConvertError:
        return

    print result

def DivCommand(args):
    #Should argument handling be handled inside each individual function or through another means
    if len(args) > 2:
        print "Error: Too many arguments to divide by"
    elif len(args) == 1:
        print "Error: Only 1 argument passed in"
    else:
        try:
            numerator = ConvertArgumentToNumber(args[0])
            denominator = ConvertArgumentToNumber(args[1])
            if denominator == 0:
                print "Error: Divide by 0"
            else:
                result = numerator / denominator
        except ArgumentConvertError:
            return

        print result

def ModuloCommand(args):
    #TODO: Implement a error reporting system to account for various types of errors in the language
    print "Command: 'modulo' is not currently implemented"


def PrintCommand(args):
    constructed_string = ""
    appending_string = False

    for argument in args:
        argument_string = str(argument)

        # found a string to append, now to construct the string
        if argument_string[0] == '"':
            constructed_string = constructed_string + str(argument)[1 : ] + " "
            appending_string = True
            
            continue

        # found the end of the string, stop constructing the string
        if argument_string[len(argument_string)-1] == '"':
            constructed_string = constructed_string + argument_string[ : len(argument_string) - 1]
            print constructed_string
            
            constructed_string = ""
            appending_string = False
            
            continue
        
        # add all words that appear in between the quotation marks to the string
        if appending_string == True:
            constructed_string = constructed_string + argument_string + " "
        else:
            print argument_string


# A dictionary to house the mappings of text to function implementations of commands
command_dict = {'hello' : HelloCommand, 'exit' : ExitCommand,'clear' : ClearCommand, 'cls' : ClearCommand, 'add' : AddCommand, '+' : AddCommand, 'sub' : SubCommand, '-' : SubCommand, 'mult' : MultCommand, '*' : MultCommand, 'div' : DivCommand, '/' : DivCommand, 'mod' : ModuloCommand, '%' : ModuloCommand, 'print' : PrintCommand}
