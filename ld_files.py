#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import subprocess


### Initialisation directory/files

def directory_prepare():

	directory_lockdown = (os.path.expanduser('~') + "/.lockdown")
	
	## Default directory creation

	print ("\n# Preparing directory & files")

	if os.path.exists(directory_lockdown):
		print ("Directory exist, nothing to do.")
		
		## Check permissions

	        print ("\n# Checking permissions")

	        if os.stat(directory_lockdown).st_mode != 16768:
	                print ("Folder have wrong permissions, correction applied.")
	                os.chmod(directory_lockdown, 0o600)
	        else:
	                print ("Folder have good permissions, nothing to do.")

	else:
		os.makedirs(directory_lockdown)
		os.chmod(directory_lockdown, 0o600)
		print ("Directory doesn't exist.. created.\n")

