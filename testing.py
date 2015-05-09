# Implementation of switches as close to the implementation as found in C++
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False


# Parses out all the words found in the whole input string 
def ParseStringInput(input_string):
    words = input_string.split()
    if len(words) == 0:
        words.append(" ")
    
    return words

def ConvertNumberArgument(string_number):
    try:
        number = int(string_number)
    except ValueError:
        number = float(string_number)

    return number

# Command Implementations
def HelloCommand(args):
    print "Hello and welcome to this little command interpreter developed and programmed by David Burns!"

def ExitCommand(args):
    pass

def AddCommand(args):
    result = ConvertNumberArgument(args[0])
    for argument in args[1 : ]:
        result = result + ConvertNumberArgument(argument)

    print result

def SubCommand(args):
    result = ConvertNumberArgument(args[0])
    for argument in args[1 : ]:
        result = result - ConvertNumberArgument(argument)

    print result

def MultCommand(args):
    result = ConvertNumberArgument(args[0])
    for argument in args:
        result = result * ConvertNumberArgument(argument)

    print result

def DivCommand(args):
    #Should argument handling be handled inside each individual function or through another means
    if len(args) > 2:
        print "Error: Too many arguments to divide by"
    elif len(args) == 1:
        print "Error: Only 1 argument passed in"
    else:
        numerator = ConvertNumberArgument(args[0])
        denominator = ConvertNumberArgument(args[1])
        if denominator == 0:
            print "Error: Divide by 0"
        else:
            result = numerator / denominator
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
command_dict = {'hello' : HelloCommand, 'exit' : ExitCommand, 'add' : AddCommand, '+' : AddCommand, 'sub' : SubCommand, '-' : SubCommand, 'mult' : MultCommand, '*' : MultCommand, 'div' : DivCommand, '/' : DivCommand, 'mod' : ModuloCommand, '%' : ModuloCommand, 'print' : PrintCommand}

def ProcessCommand(command, args):
    if command_dict.has_key(command):
        command_call = command_dict[command]
        if hasattr(command_call, '__call__'):
            command_call(args)
        else:
            print "The command: '" + command + "' is not able to be executed"
    else:
        print "The command: '" + command + "' is not currently defined"

if __name__ == "__main__":
    input_command = ""
    input_args = []

    while input_command != "exit":
        user_input = raw_input("> ")
        
        input_words = ParseStringInput(user_input)
        input_command = input_words[0]
        input_args = input_words[1 : ]

        ProcessCommand(input_command.lower(), input_args)
        
