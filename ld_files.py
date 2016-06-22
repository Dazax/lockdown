#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import subprocess


### Initialisation directory/files

def directory_prepare():

	directory = (os.path.expanduser('~') + "/.lockdown")
	
	## Default directory creation

	print ("\n# Preparing directory & files")

	if os.path.exists(directory):
		print ("Directory exist, nothing to do.\n")
	else:
		os.makedirs(directory)
		print ("Directory doesn't exist.. created.\n")
