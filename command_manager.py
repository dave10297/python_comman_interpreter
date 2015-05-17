class Command(object):
    def __init__(self, command_string, command_function):
        self.command_str = command_string
        self.command_func = command_function

    def call(self, args):
        if hasattr(self.command_func, "__call__"):
            self.command_func(args)
        else:
            print "Error: '{0}' could not be executed".format(self.command_string)

    def __str__(self):
        print self.command_str

class CommandManager(object):
    # The constructor sets up the command list,
    def __init__(self, command_imp_dict):
        self.command_list = []

        command_imp_dict["help"] = self.HelpCommand
        for command_key in command_imp_dict:
            new_command = Command(command_key, command_imp_dict[command_key])
            self.command_list.append(new_command)

    def ProcessCommand(self, input_command, input_args):
        for command in self.command_list:
            if command.command_str == input_command:
                command.call(input_args)
                return
        
        print "Error: '{0}' is not currently defined".format(input_command)

    
    # I have to define the help command here to avoid scope issues with the command dictionary, hope to change this in the future
    def HelpCommand(self, args):
        print "The commands currently availabel: "
        print self.command_list
