####################################
# accParser_append.py
#
# Special version of accParser.py
# Used when there are separate epochs for a single run.
# !!BE CAREFUL!! -- THIS WORKS ONLY WHEN FILES ARE NAMED USING A FIXED SCHEME AND THIS SCRIPT IS APPLIED ON THOSE FILES IN A CERTAIN ORDER
####################################
import sys

if (len(sys.argv) != 2):
	print "Exiting Program....\nUsage: python accParser.py /path/to/screen/output"


dataPath = sys.argv[1] #the first argument is the path to the screen grab of the TF Learn run

dataFile = open(dataPath, 'r')
outFile = open(dataPath[:-6] + 'out.txt', 'a') # !!HIGHLY UNSTABLE LINE!!

#outFile.write("epoch loss acc val_acc\n")
resultLines = dataFile.readlines()

for line in resultLines:
	if 'val_acc' in line:
		words = line.split()
	
		#validation step
		if words[-2:-1] != ['iter:']:
			print "Something doesn't look right. Skipping an occurence of val_acc"
			continue

		outFile.write(words[words.index("epoch:")+1] + " ")		
		outFile.write(words[words.index("loss:")+1] + " ")		
		outFile.write(words[words.index("acc:")+1] + " ")		
		outFile.write(words[words.index("val_acc:")+1] + "\n")		

dataFile.close()
outFile.close()
