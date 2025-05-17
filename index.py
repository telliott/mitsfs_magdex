#!/usr/bin/python3
import os
import urllib.parse
import json
from magdex import magazine
from magdex import frontpage

# comment this out for the actual site
import cgitb
cgitb.enable()

#URL to the main magazine page
top_url = os.environ["REQUEST_URI"].split('?')[0]

#URL to magazines (tells the frontpage how to construct a magazine link). Actual mag link 
#will be substituted into the [] sections
magazine_url = top_url + "?mag=[SECTION]/[MAG]"

# Path to root folder where magazine folders are		
magazine_root = os.environ["CONTEXT_DOCUMENT_ROOT"] + "/mitsfs_magdex/magazines/"

#query parameters
params = urllib.parse.parse_qs(os.environ["QUERY_STRING"])


print ("Content-type: text/html\r\n\r\n")
print ("<!DOCTYPE html>\n")
print (('<html>\n<head>'
  		'<link rel="stylesheet" href="http://mitsfs.mit.edu/static/css/main.bdbe7b61a7bbc1d899d2d4c72c413f96.css">'
  		'<style>td {padding: 15px;} th {padding: 15px;}</style>'
		'</head>\n<body>'))

if "mag" in params:

	#put in a link back to the main page
	print ("<a href=\"%s\">Back</a>\n" % top_url)
	(folder, mag) = params["mag"][0].split("/" , 1)
	
	print (magazine.createMagazine(folder, mag, magazine_root))
else:
	print (frontpage.createFrontpage(magazine_root, magazine_url))

print ("</body>\n</html>")
