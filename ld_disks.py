#!/usr/bin/python
# -*- coding: utf-8 -*-


import subprocess


### Disk Choice

def disk_choice():

	## List disks & add to dictionnary

	disk_listing = subprocess.Popen(['blkid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	disk_choice = 0
	disk_dico = {}

	print ("\n# Here is the available disks #\n")

	for line in iter(disk_listing.stdout.readline, b''):
		disk_dico[disk_choice] = line.rstrip().split(":")[0]
		print(str(disk_choice) + " >>> " + line.rstrip()).split(":")[0]
		disk_choice += 1

	## Make choice of disk
	
	print ("99 >>> Back to main menu")

	print ("\n# Make your choice:")
	disk_used = input()
	
	if disk_used == 99:
		return
	
	if disk_used not in range(disk_choice):
               	print ("\n# Error")
		print ("Something wrong with your choice, exiting..")
               	exit(1)
	
	if disk_used in range(disk_choice):
		print ("\n# Confirmation")
		print ("Are you sure to use : " + disk_dico[disk_used] + " [y/n] :") 
		disk_used_validation = raw_input()

		if disk_used_validation not in ("y", "Y", "n", "N"):
			print ("\n# Error")
			print ("Something wrong with your choice, exiting..")
			exit(1)

		return disk_dico[disk_used]


### Initialisation disk & directory/files

#def disk_prepare(disk):

	## Initialisation for use with lockdown
	## Todo : Format disk & co


### Mounting Disk + Pairing USB/User

#def disk_pairing():
