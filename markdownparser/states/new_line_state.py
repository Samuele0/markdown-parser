from .parsing_state import ParsingState


class NewLineState(ParsingState):

    def __init__(self, document_node=None):
        super().__init__()
        self.document_node = document_node

    def accept(self, char, state_manager):
        cases = {
            " ": lambda: self,
            "\t": lambda: self,
            "#": lambda: state_manager.get('header')(),
            "*": lambda: state_manager.get('bold_or_enum')()

        }
        return cases.get(char, state_manager.get('text'))()
