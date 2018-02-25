# takes tflearn output and extracts loss, acc every epoch for visualization

path = '../runResults/alex_opt_run_1_n2.txt' # all results if in a separate folder
results = open(path, 'r')
lossList = open(path + '_loss.txt', 'w')
accList = open(path + '_acc.txt', 'w')
valAccList = open(path + '_valAcc.txt', 'w')
resultLines = results.readlines()
for line in resultLines:
	if 'val_acc' in line:
		# print(line[20:23]) # this is the epoch (in the output files, the line number is the epoch)
		lossList.write(line[32:39] + '\n') # loss
		accList.write(line[47:53] + '\n') # accuracy
		valAccList.write(line[85:91] + '\n') # val accuracy
results.close()
lossList.close()
accList.close()
valAccList.close()
