#filter not_empty string in a list

def not_empty(s):
	return s and s.strip()

print filter(not_empty , ['A' , '' , 'B' , None , 'C' , '   '])