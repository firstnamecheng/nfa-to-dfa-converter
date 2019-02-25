from State import State
from DfaState import DfaState


def make_dfa( nfastate ):
    if nfastate.type == "initial":
        states = list()
        states.append( nfastate )
        lambda_trans = nfastate.transitions[ "lambda" ]
        if lambda_trans.__len__() > 0:
            for state in lambda_trans:
                states.append( state )
        new_dfa = DfaState( states, nfastate.transitions.keys() )
        new_dfa.type = "initial"
        new_dfa.set_name()
        new_dfa.check_type()
        return new_dfa


def help_nfa():
    print( "Add transition example: qM > a > qN" )
    print( "Enter 'qX setinitial' to set as initial state")
    print( "Enter 'qX setfinal' to set as final state" )
    print( "Enter 'done' to create dfa\n" )


def help_dfa():
    print( "Enter 'view' to view name and type of current state" )
    print( "To see transition on x, enter 'transition x'" )
    print( "To move to next node on transition x, enter 'process x'" )
    print( "To go back to initial/start state, enter 'initial'" )
    print( "Enter 'done' when finished\n")


def nfa_loop( nfa_states ):
    print( "Enter 'help' to see usage for editing NFA\n" )
    editing_nfa = True
    while editing_nfa:
        action = input( "Enter a command: " )
        if action == "help":
            help_nfa()
        elif action.__contains__( ">" ):
            args = action.split( ">" )
            nfa1_index = int( args[ 0 ].strip()[ 1 ] )
            nfa2_index = int( args[ 2 ].strip()[ 1 ] )
            nfa1 = nfa_states[ nfa1_index ]
            nfa2 = nfa_states[ nfa2_index ]
            transition = args[ 1 ].strip()
            nfa1.add_transition( transition, nfa2 )
        elif action.__contains__( "set" ):
            args = action.split()
            nfa_index = int( args[ 0 ].strip()[ 1 ] )
            type = args[ 1 ].strip()[ 3: ]
            nfa_states[ nfa_index ].type = type
        elif action == "done":
            nfa_states[ 0 ].type = "initial"
            break
        else:
            print( "Command '" + action + "' not recognized." )


def dfa_loop( nfa_states ):
    current_dfa = make_dfa( nfa_states[ 0 ] )
    initial = current_dfa
    print( "Enter 'help' to see usage for viewing DFA\n" )
    viewing_dfa = True
    while viewing_dfa:

        action = input( "Enter command: " )
        if action == "help":
            help_dfa()
        elif action == "view":
            current_dfa.see_dfa()
        elif action.__contains__( "transition" ):
            current_dfa.make_transitions()
            transition = action.split()[ 1 ].strip()
            next_dfa = DfaState( current_dfa.transitions[ transition ],
                                 current_dfa.transitions.keys() )
            next_dfa.set_name()
            next_dfa.check_type()
            next_dfa.see_dfa()
        elif action.__contains__( "process" ):
            current_dfa.make_transitions()
            transition = action.split()[ 1 ].strip()
            current_dfa = DfaState( current_dfa.transitions[ transition ],
                                    current_dfa.transitions.keys() )
            current_dfa.set_name()
            current_dfa.check_type()
        elif action == "initial":
            current_dfa = initial
        elif action == "done":
            break
        else:
            print( "Action not recognized" )






def main():
    num_trans = input( "Input transitions (i.e. 'a,b,c'): " )
    trans = num_trans.split( "," )
    for i in range( len( trans ) ):
        trans[ i ] = trans[ i ].strip()

    num_states = int( input( "Input number of nfa states/nodes: " ) )
    nfa_states = list()

    print_out = "States: "
    for n in range( num_states ):
        new_nfa_state = State( "q" + str( n ), trans )
        nfa_states.append( new_nfa_state )
        print_out += "q" + str( n ) + ", "
    print_out = print_out[ :-2 ] + " created."
    print( print_out )

    nfa_loop( nfa_states )
    dfa_loop( nfa_states )


if __name__ == "__main__":
    main()
