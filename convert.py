#!/usr/bin/python

from os import listdir, system
from os.path import isfile, join
print "Welcome to the video-mp3 convertor:\n"

source_folder = str(raw_input("Enter full path to the source folder : "))
target_folder = str(raw_input("Enter the full path to the destination folder : "))
print "Starting\n\n"
for f in listdir(source_folder):
	if isfile(join(source_folder, f)):
		command = "avconv -i \'{}{}\' -vn -f mp3 \'{}{}.mp3\'".format(source_folder,f, target_folder, f)
		system(command)
		# print command
print "\n_________\nprocess complete \n ______\n"

