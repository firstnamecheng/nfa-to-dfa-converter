from State import State
from DfaState import DfaState


def make_dfa( nfastate ):
    if nfastate.type == "initial":
        states = [ nfastate ]
        lambda_trans = nfastate.transitions[ "lambda" ]
        if lambda_trans.__len__() > 0:
            for state in lambda_trans:
                states.append( state )
        new_dfa = DfaState( states, nfastate.transitions.keys() )
        new_dfa.type = "initial"
        return new_dfa


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


def help_nfa():
    print( "Add transition example: qM > a > qN" )
    print( "Enter 'qX setinitial' to set as initial state")
    print( "Enter 'qX setfinal' to set as final state" )
    print( "Enter 'done' to create dfa" )


def main():
    num_trans = input( "Input transitions (i.e. 'a,b,c'): " )
    trans = num_trans.split( "," )
    for i in range( len( trans ) ):
        trans[ i ] = trans[ i ].strip()

    num_states = int( input( "Input number of nfa states/nodes: " ) )
    nfa_states = list()
    for n in range( num_states ):
        new_nfa_state = State( "q" + str( n ), trans )
        nfa_states.append( new_nfa_state )

    print( "Enter 'help' to see usage" )
    editing_nfa = True
    while editing_nfa:
        action = input( "Enter a command: " )
        if action == "help":
            help_nfa()
        elif action.__contains__( ">" ):
            args = action.split( ">" )
            nfa1 = int( args[ 0 ].strip()[ 1 ] )
            nfa2 = int( args[ 2 ].strip()[ 1 ] )
            transition = args[ 1 ].strip()
            nfa_states[ nfa1 ].transitions[ transition ].append( nfa2 )
        elif action.__contains__( "set" ):
            args = action.split()
            nfa = int( args[ 0 ].strip()[ 1 ] )
            type = args[ 1 ].strip()[ 3: ]
            nfa_states[ nfa ].type = type
        elif action == "done":
            break
        else:
            print( "Command '" + action + "' not recognized." )


if __name__ == "__name__":
    main()