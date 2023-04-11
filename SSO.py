# Renames all files in screenshots directory
# Gets last modified date and renames file to that

import os, time, re
from datetime import datetime

rootdir = 'H:/System/Pictures/Screenshots/'
ssdir = 'H:/System/Pictures/Screenshots/All/'

fn = 0 # File number
fee = 0 # FileExistsError

s = time.time()

for root, dirs, files in os.walk(rootdir):
	for fname in files:
		if re.match(r'^Screenshot \([0-9]+\)',fname):
			fext = os.path.splitext(fname) # Get file extension
			lmt = os.path.getctime(rootdir+fname) # Last Modified Time
			dt = datetime.fromtimestamp(lmt).strftime('%Y-%m-%d_%H-%M-%S')
			
			cn = rootdir+fname # Current name
			nn = ssdir+dt+fext[1] # newname
			
			try:
				rn = os.rename(cn,nn)
			except FileExistsError:
				fee += 1
				nn = ssdir+dt+' ('+str(fee)+')'+fext[1] # newname
				rn = os.rename(cn,nn)

			print('>> Renamed "'+fname+'" to "'+dt+fext[1]+'"')
			fn += 1
		else:
			pass

input('\n\n\n>> Renamed '+str(fn)+' files in '+str(time.time()-s)+' secs')