import sgf

import os  
for fn in os.listdir('.'):
     if os.path.isfile(fn):
        print (fn)
with open("/Users/hemingwei/Documents/MUM/BDT/Project/kgs-19-2018-02-new/2018-02-01-1.sgf") as f:
	collection = sgf.parse(f.read())
for gameTree in collection:
	cnt = 0
	for node in gameTree:
		print(cnt)
		for key, values in sorted(node.properties.items()):
			print key
			for value in values:
                		print("[%s]" % value)
		cnt += 1

				
		

	
	
		
	
