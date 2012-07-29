import os
import glob

if not os.path.exists('mp3'):
	os.mkdir('mp3')

for f in glob.glob('*.ogg'):
	newName = f.replace('.ogg', '.mp3')
	
	print "Converting " + f
	os.system('sox "' + f + '" "mp3/' + newName + '"')
