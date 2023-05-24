class GrammarError(Exception):
    def __init__(self, message, at):
        self.message = message
        self.at = at