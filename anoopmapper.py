#!/usr/bin/python

import sys
import re
import os

def main(argv):
 
	reg = re.compile("^[^a-z]") 
	filepath = os.environ["map_input_file"]
	(a1, a2, a3, a4) = filepath.strip().split("-")
	for line in sys.stdin:
		(c1, c2, c3, c4) = line.strip().split( )
		if(c1 == 'en'):
			if(not c2.startswith('Media') and not c2.startswith('Special') and not c2.startswith('Talk') and not c2.startswith('User') and not c2.startswith('User_talk')  and not c2.startswith('Project' ) and not c2.startswith('Project_talk') and not c2.startswith('File') and not c2.startswith('File_talk') and not c2.startswith('MediaWiki')  and not c2.startswith('MediaWiki_talk') and not c2.startswith('Template') and not c2.startswith('Template_talk') and not c2.startswith('Help') and not c2.startswith('Help_talk') and not c2.startswith('Category') and not c2.startswith('Category_talk') and not c2.startswith('Portal') and not c2.startswith('Wikipedia') and not c2.startswith('Wikipedia_talk')):
				if(reg.match(c2)):
					if(not c2.endswith('.jpg') and not c2.endswith('.gif') and not c2.endswith('.png') and not c2.endswith('.JPG') and not c2.endswith('.GIF') and not c2.endswith('.PNG') and not c2.endswith('.txt' ) and not c2.endswith('.ico')):
						if(c2 != '404_error/' and c2 != 'Main_Page' and c2 != 'Hypertext_Transfer_Protocol' and c2 != 'Favicon.ico' and c2 != 'Search'):
							print c2 + "\t" + c3 + "\t" + a3 
  
 
 
   
if __name__ == "__main__":
 main(sys.argv)