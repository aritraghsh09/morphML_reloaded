####################################
# accParser.py
#
# Takes tflearn screen output and extracts loss, acc and val_acc every epoch for visualization
####################################
import sys

if (len(sys.argv) != 2):
	print "Exiting Program....\nUsage: python accParser.py /path/to/screen/output"


dataPath = sys.argv[1] #the first argument is the path to the screen grab of the TF Learn run

dataFile = open(dataPath, 'r')
outFile = open(dataPath[:-6] + 'out.txt', 'w')

outFile.write("epoch loss acc val_acc\n")
resultLines = dataFile.readlines()

for line in resultLines:
	if 'val_acc' in line:
		words = line.split()
	
		#validation step
		if words[-2:-1] != ['iter:']:
			print "Something doesn't look right. Skipping an occurene of val_acc"
			continue

		outFile.write(words[words.index("epoch:")+1] + " ")		
		outFile.write(words[words.index("loss:")+1] + " ")		
		outFile.write(words[words.index("acc:")+1] + " ")		
		outFile.write(words[words.index("val_acc:")+1] + "\n")		

dataFile.close()
outFile.close()
