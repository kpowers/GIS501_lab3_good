##GIS501 Lab 3 Problem 1
##rename files in a directory and change them to lower case

import os #import os module for the os.walk function good site:http://www.pythoncentral.io/how-to-traverse-a-directory-tree-in-python-guide-to-os-walk/

#set the directory you want to start from

mydir = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_Data_L3/text_files/"
new_dir = "D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_Data_L3/text_files_new/" #must create this folder for code to work.
badext = ['.text', '.py', '.rtf']
for root, dirs, files in os.walk ('D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_Data_L3/text_files'):
	for file_name in files:
		temp_name = file_name.lower()
		for thing in badext:
			if thing in file_name:
				new_name = temp_name.replace(thing, '.txt')
				print new_name
				os.rename(mydir + file_name, new_dir + 'file_' + new_name)
