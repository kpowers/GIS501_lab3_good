##GIS 501 - Lab 3 problem 4 Create a turtle
##You are going to write a script that asks the user to input a number and then draws a shape with that number of sides!

import turtle					#allows us to use the turtles library	
wn = turtle.Screen()                            #creates a graphics window
turtle.speed                                    #gives turtle max speed
wn.bgcolor('lightblue')		                #background color to light blue
alex = turtle.Turtle() 			        #create a turtle named alex
alex.color('darkgreen')
# alex.forward(150)				#tell alex to move forward by 150 units
# alex.left(90)					#turn by 90 degrees
# alex.forward(75)				#complete the second side of a rectangle

print ("This program draws shapes based on the number you enter in a uniform pattern.")
num_sides = int(input("Enter the number of sides for an equilateral polygon the turtle will draw: "))
    
angle = int(360/num_sides)                      #divide the inside angle by number of sides input by user to determine angle that the turtle turns.

for num_sides in range (num_sides):
    alex.forward(50)                            #length of each line segment
    alex.left(angle)

turtle.mainloop()                               #keeps turtle draw window from freezing
    
    




