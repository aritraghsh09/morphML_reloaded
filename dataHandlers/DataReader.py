# splits master csv into separate lists to wget

masterCSV = open('ZooMaster.csv')
spiralList = open('spiralList.txt', 'w')
ellipticalList = open('ellipticalList.txt', 'w')
uncertainList = open('uncertainList.txt', 'w')

allLines = masterCSV.readlines()
counter = 0
total = len(allLines)
del allLines[0] # header
for line in allLines:
	lineArray = line.split(',')
	if lineArray[2] == '1':
		spiralList.write(lineArray[1] + '\n')
	elif lineArray[3] == '1':
		ellipticalList.write(lineArray[1] + '\n')
	else:
		uncertainList.write(lineArray[1] + '\n')
	counter += 1
	print(counter / total)
	