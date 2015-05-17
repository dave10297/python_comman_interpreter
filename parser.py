class InputParser(object):
    def __init__(self):
        pass

    def Parse(self, string_input):
        words = string_input.split()
        if len(words) == 0:
            words.append(" ")
    
        return words
        
