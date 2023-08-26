##CS 101
##Program 1
##Christina Gerstner
##clgdtf@mail.umkc.edu
##
##Problem: A new graphics file format called turtle has been created and you are tasked
##      writing a python program to read the data from the file and using the turtle
##      module to draw the shapes from the file. This assignment will have you using
##      your skills with file handling, error handling, string manipulation and using
##      the turtle module. To make this easier you should use your newfound knowledge
##      of functions to break the program down into smaller testable portions. You will
##      be required to use functional decomposition in your assignments from this
##      assignment on.
##
##ALGORITHM:
##      1. ask user for pronunciation.
##      2. validate whether or not user input has valid characters for translation
##      3. for loop that checks each char and adds correct ordinal value prununciation to an
##         empty string
##      4. print out tranlated pronunciation
##      5. ask user if they want to enter another word
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: None
##################################################################################################
import turtle

def determineShapeFile(fileName):
	if fileName == 'rectangle.tff':
		return True
	elif fileName == 'circle.tff':
		return True
	elif fileName == 'star.tff':
		return True
	elif fileName == 'pythonlogo.tff':
		return True
	elif fileName == 'badcommand.tff':
		return True
	elif fileName == 'rectangle_value_error.tff':
		return True
	elif fileName == 'rectangle_index_error.tff':
		return True
	else:
		return False

def drawShape(shapeFile):
	shapeDetails = open(shapeFile)
	lines = shapeDetails.readlines()

	if shapeFile == 'rectangle.tff':
		#draw_rectangle(x, y, width, height, color)
		for line in lines:
		    lineList = line.split(',')
		    del lineList[0]
		    x_val = int(lineList[0])
		    y_val = int(lineList[1])
		    width_val = int(lineList[2])
		    height_val = int(lineList[3])
		    colorName = lineList[4]
		    draw_rectangle(x_val, y_val, width_val, height_val, colorName)

	elif shapeFile == 'circle.tff':
		#draw_circle(x, y, radius, color)
		for line in lines:
		    lineList = line.split(',')
		    del lineList[0]
		    x_val = int(lineList[0])
		    y_val = int(lineList[1])
		    radius_val = int(lineList[2])
		    colorName = lineList[3]
		    draw_circle(x_val, y_val, radius_val, colorName)

	elif shapeFile == 'star.tff':
		#draw_star(x, y, width, height, color)
		for line in lines:
		    lineList = line.split(',')
		    del lineList[0]
		    x_val = int(lineList[0])
		    y_val = int(lineList[1])
		    width_val = int(lineList[2])
		    height_val = int(lineList[3])
		    colorName = lineList[4]
		    draw_star(x_val, y_val, width_val, height_val, colorName)

	elif shapeFile == 'pythonlogo.tff':
		#draw_pythonlogo(x, y) #more parameters are probably needed
		#pythonlogo joke - 'I'm so sorry.', pythonlogo, 'is currently undergoing construction. Please try again at a later time.'

#rectangle & cicle function go here

def draw_star(x : int, y : int, width : int, height : int, color : str):
    star = turtle.Turtle()
    turtle.setx(x)
    turtle.sety(y)

    star.color(color)
    star.begin_fill()
    for i in range(5):
        star.forward(200)
        star.right(144)
    star.end_fill()
    turtle.done()

	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			width : int - The width of the rectangle to be drawn
			height : int - The height of the rectangle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# use turtle to draw lines of 3 star in different locations
	# use fill method to color stars from star.tff

#def draw_pythonlogo_4(x : int, y : int, width : int, height : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			width : int - The width of the rectangle to be drawn
			height : int - The height of the rectangle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# use turtle to draw lines of all shapes w/ 4 sides in different locations
	# use fill method to color shapes from pythonlogo.tff

#def draw_pythonlogo_3(x : int, y : int, radius : int, color : str) -> None:
	""" Draws a circle with turtle at the point x, y with the given radius
		Parameters :
			x : int - The x position of the center of the circle.
			y : int - The y position of the center of the circle.
			radius : int - The radius of the circle to be drawn
			color : str - The color of the circle and the fill color
		returns : None
	"""
	# use turtle to draw curves of all shapes in different locations
	# use fill method to color shapes from pythonlogo.tff

exist = True
while exist:
	userFile = input('Enter File to open & draw ==>\t')

	if userFile.lower() == 'quit':
		exist = False

	validateFile = determineShapeFile(userFile)
	if validateFile == False:
		print('Could not open file :', userFile)
	else:
		if userfile == 'badcommand.tff' or userfile == 'rectangle_value_error.tff' or userfile == 'rectangle_index_error.tff':
			file = open(userFile)
			content = file.readlines()
			file.close()

			for line in content:
				print(line)
		else:
			drawShape(userFile) # drawShape(shapeFile) function



