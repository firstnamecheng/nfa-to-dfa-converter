from dataclasses import dataclass


@dataclass
class State:
    def __init__( self, name, transitions ):
        self.name = name
        self.type = "nd"    # Initial, final, nd
        self.transitions = dict()
        for transition in transitions:
            self.transitions[ transition ] = list()
        self.transitions[ "lambda" ] = list()

    def process_char( self, char ):
        return self.transitions[ char ]

    def add_transition( self, transition, next_state ):
        self.transitions[ transition ].append( next_state )


q0 = State( "q0", ["a", "b"] )
q1 = State( "q1", ["a", "b"] )
q2 = State( "q2", ["a", "b"] )

q0.add_transition( "a", q1 )
1