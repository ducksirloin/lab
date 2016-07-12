fname = "strfile.txt"
f = open(fname,"w")
f.write("set default PBradii mbondi2" + "\n")
a = -180
for i in range(0,361):
	f.write("str" + str(i) + " = sequence{ACE GLH NME}" + "\n")
	f.write("impose str" + str(i) + " {2} {{OE1 CD OE2 HE2 " + str(a+i) + "}}" + "\n")
	f.write("saveAmberParm str" + str(i) + "  confamb" + str(i) + ".prmtop confamb" + str(i) + ".inpcrd" + "\n")

