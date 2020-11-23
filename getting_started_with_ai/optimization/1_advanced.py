portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
	if not ports:
		print(' '.join([portnames[i] for i in route]))
	else:
		for i in ports:
			route.append(i)
			permutations(route, ports[i:])

# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
