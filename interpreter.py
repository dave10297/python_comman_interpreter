from command_manager import *
from command_implements import*
from parser import*

class Interpreter(object):
    def __init__(self):
        self.command_manager = CommandManager(command_dict)
        self.input_parser = InputParser()

    def Run(self):
        is_running = True
        while is_running == True:
            user_input = raw_input("> ")
            if user_input == "exit":
                is_running = False

            input_words = self.input_parser.Parse(user_input)
            input_command = input_words[0]
            input_args = input_words[1 : ]

            self.command_manager.ProcessCommand(input_command.lower(), input_args)
