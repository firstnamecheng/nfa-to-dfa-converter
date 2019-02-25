from dataclasses import dataclass


@dataclass
class State:
    def __init__( self, name, transitions ):
        self.name = name
        self.type = "nd"    # initial, final, nd
        self.transitions = dict()
        for transition in transitions:
            self.transitions[ transition ] = list()
        self.transitions[ "lambda" ] = list()

    def add_transition( self, transition, next_state ):
        on_transition = self.transitions[ transition ]
        State.add_no_dup( on_transition, next_state )

    @staticmethod
    def add_no_dup( collection, state ):
        for nfastate in collection:
            if nfastate.name == state.name:
                return
        collection.append( state )

