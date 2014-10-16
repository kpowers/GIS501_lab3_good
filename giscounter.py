##GIS 501 Lab 3 Problem 2
##Module that counts the number of times that science and systems appear in the file GIS_is_the_best.txt

##open the file GIS_is_the_best.txt
gis_file = open('I:/GIS501_AU_2014_Directory/GIS501_Labs/GIS501_Lab_3/GIS501_RAWDATA_L3/lab3/GIS_is_the_best.txt')
file_list = gis_file.read()

system_count = 0
science_count = 0
total_words = 0

for word in file_list.split(' '): #creates a list from every word in the GIS_is_the_best.txt file
        if word.lower()== 'systems':
                system_count = system_count + 1
        elif word.lower() == 'science':
                science_count = science_count + 1
        else:
                total_words = total_words + 1

total_words = system_count + science_count + total_words
print total_words
