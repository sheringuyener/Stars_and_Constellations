import turtle
WIDTH = turtle.window_width() / 2.0

def convertXY(origX, origY, width):
       '''Takes origX and origY in the star coordinate system and returns
        x and y in the screen coordinate system'''
       # FILL IN CODE




       
def drawStar(origX, origY, t, brightness, col):
       """ First, calls convertXY to convert origX and origY to the screen
       coordinates. Then uses the turtle t and color col to draw a circle
       at position x,y and with radius proporional to the brightness."""
       # FILL IN CODE




       
      
       
def drawLine(origX1, origY1, origX2, origY2, t, col):
       '''First calls convertXY to convert (origX1, origY1) and (origX2, origY2)
       to screen coordinates (x1, y1) and (x2, y2).Then uses the turtle t
       to draw a line between points (x1,y1) and (x2, y2)'''
       # FILL IN CODE
       


       

def loadStars(filename, t):
       ''' Reads stars from the file, calls drawStar for each star.
       Creates and returns a dictionary containing (key, value) pairs,
       where key is the name of the star, and value is (x, y) position.
       Also, it should compute which star is the brightest, write this
       message on the screen and highlight it in green.'''
       # FILL IN CODE
       
       

def drawConstellations(dictStars, constelFilename, t):
       ''' Reads the constellation file and calls drawLine for
       each pair of stars'''
              

       
def main():
       
       # Create screen and turtle
       import turtle
       scr = turtle.Screen()
       # FILL IN CODE
       
       
       scr.tracer(0) # do not update the screen

       # Call loadStars and get the dictionary of stars
       # FILL CODE

       # Read constellation files (assumes they are in the current directory)
       import glob
       listFiles = glob.glob("*_lines.txt")
       for filename in listFiles:
           print(filename)
           # Call draw constellations here
           # FILL IN CODE
           
           
       scr.update() # update the screen
       scr.tracer(10)

main()   # call main
