from State import State
from DfaState import DfaState


def make_dfa( nfastate ):
    if nfastate.type == "initial":
        states = [ nfastate ]
        lambda_trans = nfastate.transitions[ "lambda" ]
        if lambda_trans.__len__() > 0:
            for state in lambda_trans:
                states.append( state )
        return DfaState( states, nfastate.transitions.keys() )


q0 = State( "q0", ["a", "b"] )
q1 = State( "q1", ["a", "b"] )
q2 = State( "q2", ["a", "b"] )

q0.add_transition( "a", q1 )
q0.add_transition( "a", q2 )
q0.type = "initial"
dfa = make_dfa( q0 )
print( q0.transitions["a"][0].name )
# print( dfa.get_name() )    <-- fix this
print( dfa.nfaStates )
