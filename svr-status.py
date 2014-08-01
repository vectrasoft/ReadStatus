import os

os.system("ps -e -o %cpu,command > data.txt")

fn = open("verbal.txt", "w")
with open("data.txt", "r") as f:
	for line in f:
		a = line.find(".")
		if a > 0:
			cent = int(line[:a])
			if cent > 0:
				cmd = line[a+3:]
				b = cmd.find("\n")
				if b > 0 and len(cmd) < 10:
					ncmd = cmd.replace("/", " ")
					if ncmd.find("[") == 0 and ncmd.find("]") == len(ncmd)-1:
						print "bracketed"
						ncmd = ncmd[1:len(ncmd)-1]
					fn.write(str(cent) + ' percent c p u used by ' + str(ncmd) + "\n")
				else:
					c = cmd.find(" ")
					cmd = str(cmd[:c])
					ncmd = cmd.replace("/", " ")
					if ncmd.find("[") == 0 and ncmd.find("]") == len(ncmd)-1:
						print "bracket"
						ncmd = ncmd[1:len(ncmd)-1]
					fn.write(str(cent) + ' percent c p u used by ' + str(ncmd) + "\n")
fn.close()
verbal = "festival_client --async --ttw --aucommand 'aplay $FILE' verbal.txt"
os.system(verbal)
#os.system("rm data.txt verbal.txt")
