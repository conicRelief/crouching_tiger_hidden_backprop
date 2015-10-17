
def levenshtein_distance(s, t):
	if not s: return len(t)
	if not t: return len(s)
	if s[0] == t[0]: return levenshtein_distance(s[1:], t[1:])
	l1 = levenshtein_distance(s, t[1:])
	l2 = levenshtein_distance(s[1:], t)
	l3 = levenshtein_distance(s[1:], t[1:])
	return 1 + min(l1, l2, l3)

def end_algorithm_is_good_idea(iteration ,userControl = False, time_out= 5000, discrete_timeout = 100):
    # This basically tells us wether or not we want to interrupt the process step by stepr
    # The interrupt stalls the main loop and asks the user for input
    if userControl is True:
        line_read = raw_input( "Press <ENTER> to perform and display next iteration. Type \"exit\" to exit this loop and display weights:  ")
        lev_d = levenshtein_distance(line_read.strip().lower(),"exit" )
        if lev_d  <=2:
            return True
        else:
            return False
    else:
        """
        Todo: Implement Timeout Mechanism. for now we just
        """
        if iteration > discrete_timeout:
            return False
        else:
            return True