import os

if not os.path.exists('mp3'):
	os.mkdir('mp3')

for f in os.listdir('.'):

	if '.ogg' in f:
		newFile = f.replace('.ogg', '.mp3')
		
		print "Converting " + f
		os.system('sox "' + f + '" "mp3/' + newFile + '"')
