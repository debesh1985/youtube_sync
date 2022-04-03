#!/usr/bin/env python3
import os
import sys
import getopt
import subprocess

cwd=os.getcwd()
english="/home/debesh/Music/1 English"
hindi="/home/debesh/Music/2 Hindi"
spanish="/home/debesh/Music/3 Spanish"
kids="/home/debesh/Music/4 Kids"
bengali="/home/debesh/Music/5 Bengali"

argv = sys.argv[1:]

try:
	opts, args = getopt.getopt (argv, "m:l:")
	
except:
	print("Error: Link(m) and Languague(l) not defined")
	
for  opt, arg in opts:
	if opt in ['-m']:
		link = arg
	elif opt in ['-l']:
		lang = arg

if lang == 'english':
	os.chdir(english)
	os.getcwd()
elif lang == 'bengali':
	os.chdir(bengali)
	os.getcwd()
elif lang == 'spanish':
	os.chdir(spanish)
	os.getcwd()
elif lang == 'kids':
	os.chdir(kids)
	os.getcwd()
elif lang == 'hindi':
	os.chdir(hindi)
	os.getcwd()
print ("Downloading %s music from link %s in %s folder" %(lang, link,os.getcwd()))

cmd='/usr/local/bin/youtube-dl --ignore-errors --output "%(title)s.%(ext)s" --extract-audio --audio-format mp3 '+link
os.system (cmd)
#subprocess.run(['/usr/local/bin/youtube-dl --ignore-errors --output "%(title)s.%(ext)s" --extract-audio --audio-format mp3 ', "link"])

print ("Download is completed")

os.chdir(cwd)

