##GIS 501 Lab 3 Problem 3
##First open file
##then read file into a variable

##then I need to replace stuff... maybe somethin like
#new_file = file_name.replace(#old stuff,new_ stuff)

#then I need to open the old file to write (w will write over)
##then write it.
##then close it.

gis_file = open('D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_RAWDATA_L3/lab3/GIS_is_the_best.txt')
file_list = gis_file.read()

new_file = file_list.replace('Science', 'Systems').replace('science', 'systems')

gis_file = open('D:/GIS_501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_RAWDATA_L3/lab3/GIS_is_the_best.txt', 'w')
gis_file.write(new_file)

gis_file.close()

