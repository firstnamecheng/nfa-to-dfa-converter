from dataclasses import dataclass
from State import State


@dataclass
class DfaState( State ):
    def __init__( self, nfaStates, transitions ):
        super().__init__( "", transitions )
        self.nfaStates = nfaStates

    def get_name( self ):
        name = ""
        for state in self.nfaStates:
            name += state.name + ", "
        name = name[ :-2 ]
        return name

    def add_nfa_state( self, state ):
        self.nfaStates.append( state )

    def make_transitions( self ):
        for transition in self.transitions.keys():
            nfaStates = list()
            new_name = self.gen_name()
            for state in self.nfaStates:
                nfaStates.append(
                    state.transitions[ transition ]
                )
            self.transitions[ transition ] = DfaState( nfaStates,
                                                       self.transitions.keys() )

1+1
