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
##      1. ask user for a file to open & draw
##      2. validate whether or not the file exists
##      3. read contents of the file, for each line -> split by (",") into an empty list,
##         determine whether command is either wanting to draw a line, circle, or a rect
##      4. draw command line/circle/rect -> assign each element from list to correct
##         parameter
##      5. for line -> set (x, y) position, set the color, set heading, draw line
##      6. for circle -> set (x, y) position, set the color fill, set the radius, draw circle
##      7. for rect -> set (x, y) position, set the color fill, set the width & height,
##         draw rect (draw from left to right, turn right 90 degrees, draw from top to bottom,
##         turn right 90 degrees, draw from right to left, turn right 90 degrees, draw from
##         bottom to up
##                              left        ->          right
##                           __________________________________
##                   up      |                                |   up
##                           |                                |
##                   /\      |                                |   ||
##                   ||      |                                |   \/
##                           |                                |
##                 bottom    |                                |   bottom
##                           ----------------------------------
##                              left        <-          right
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: Program doesn't draw "pythonlogo.tff" correctly
###############################################################################################
import turtle
import os

def verifyFileExists(fileName):
	return os.path.isfile(fileName)

def readCommands(fileName):
	file = open(userfile)
	lines = file.readlines()
	file.close()
	return lines

def drawCommand(line):
	try:
		lineList = line.split(',')
		cmd = lineList[0].lower()
		if cmd == 'line':
			drawLine(line)
		elif cmd == 'circle':
			 drawCircle(line)
		elif cmd == 'rect':
			drawRect(line)
		else:
			print('Bad command given could not interpret')
	except ValueError:
		print('Could not convert an argument to int')

def drawLine(line):
	lineList = line.split(',')
	# check proper number of arguments
	if len(lineList) != 6:
		print('The line did not have proper number of arguments.')
		return
	# parameters (x, y, heading, distance, color)
	x = int(lineList[1])
	y = int(lineList[2])
	heading = int(lineList[3])
	distance = int(lineList[4])
	colorName = lineList[5].replace('\n','').replace(' ','')
	# draw shape
	shape = turtle.Turtle()
	shape.penup()
	shape.setpos(x, y)
	shape.pendown()
	shape.color(colorName)
	shape.setheading(heading)
	shape.forward(distance)

def drawCircle(line):
	lineList = line.split(',')
	# check proper number of arguments
	if len(lineList) != 5:
		print('The line did not have proper number of arguments.')
		return
	# parameters (x, y, radius, color)
	x = int(lineList[1])
	y = int(lineList[2])
	radius = int(lineList[3])
	colorName = lineList[4].replace('\n','').replace(' ','')
	# draw shape
	shape = turtle.Turtle()
	shape.penup()
	shape.setpos(x, y)
	shape.pendown()
	shape.color(colorName)
	shape.begin_fill()
	shape.circle(radius)
	shape.end_fill()

def drawRect(line):
	lineList = line.split(',')
	# check proper number of arguments
	if len(lineList) != 6:
		print('The line did not have proper number of arguments.')
		return
	# parameters (x, y, width, height, color)
	x = int(lineList[1])
	y = int(lineList[2])
	width = int(lineList[3])
	height = int(lineList[4])
	colorName = lineList[5].replace('\n','').replace(' ','')
	# draw shape
	shape = turtle.Turtle()
	shape.penup()
	shape.setpos(x, y)
	shape.pendown()
	shape.color(colorName)
	shape.begin_fill()
	shape.forward(width)
	shape.right(90)
	shape.forward(height)
	shape.right(90)
	shape.forward(width)
	shape.right(90)
	shape.forward(height)
	shape.end_fill()

fileExists = True
while fileExists:
	userfile = input('Enter File to open & draw ==>\t')

	if userfile.lower() == 'quit':
		fileExists = False
		break

	validateFile = verifyFileExists(userfile)
	if validateFile == False:
		print('Could not open file :', userfile)
	else:
		lines = readCommands(userfile)
		for line in lines:
			drawCommand(line)

