#!/usr/bin/python
# -*- coding: utf-8 -*-

import ld_disks
import ld_files


def lockdown_menu():
	# Selection Menu
	print ("# Lockdown Menu")
	print ("\n0 >>> Install/Configure requirements")
	print ("1 >>> Prepare disk to use with lockdown")
	print ("99 >>> Quit Lockdown")
	
	menu_selection00 = input()
	
	if menu_selection00 == 0:
		# Creation necessary folders/files
		ld_files.directory_prepare()
		lockdown_menu()
	elif menu_selection00 == 1:
		# Choice disk to use
		disk = ld_disks.disk_choice()
		lockdown_menu()
	elif menu_selection00 == 99:
		print ("\nExiting, bye..")
		exit(0)
	else:
		# Not allowed
		print ("Something wrong with your choice, exiting..")
		exit(1)

lockdown_menu()



# Mounting & preparation of disk
