from dataclasses import dataclass
from State import State


@dataclass
class DfaState( State ):
    def __init__( self, nfaStates, transitions ):
        super().__init__( "", transitions )
        self.nfaStates = nfaStates

    def set_name( self ):
        name = ""
        for state in self.nfaStates:
            name += state.name + ", "
        name = name[ :-2 ]
        self.name = name

    def add_nfa_state( self, state ):
        State.add_no_dup( self.nfaStates, state )

    def make_transitions( self ):
        for transition in self.transitions.keys():
            new_nfaStates = list()
            for state in self.nfaStates:
                for next in state.transitions[ transition ]:
                    State.add_no_dup( new_nfaStates, next )
            self.transitions[ transition ] = new_nfaStates

    def see_dfa( self ):
        print( self.name + ", type: " + self.type )

    def check_final( self ):
        for state in self.nfaStates:
            if state.type == "final":
                self.type = "final"
