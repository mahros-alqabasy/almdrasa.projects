# Created by Mahros


# make it reusable
def solve(ipath:str, opath:str, poss:[]):
	ifile = open(ipath, "rt").readlines()
	ofile = open(opath, "wt")

	# process
	for n in poss:
		ifile[n-1] = str(ifile[n-1]).lower()

	result = "".join(ifile).replace("\n", " ")
	ofile.write(result)
	return result




# test it
out = solve("./strings", "./output", [1, 3])
print(out)
