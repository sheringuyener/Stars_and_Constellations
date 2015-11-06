#project3.py

import turtle
WIDTH = turtle.window_width() / 2.3


def convertXY(origX, origY, width): #converts original x,y coordinates from txt file and scale them to size of window
       x=origX*width
       y=origY*width
       return (x,y)
       
def drawStar(origX, origY, t, brightness, col): #draws each star, with brightness times a factor of 3/10
       scrCoords=convertXY(origX,origY,WIDTH)
       t.color(col)
       t.up()
       t.goto(scrCoords)
       t.down()
       t.begin_fill()
       t.circle(.3*brightness)
       t.end_fill()
       
       
def drawLine(origX1, origY1, origX2, origY2, t, col): #calls convertXY, then draws line between two stars
       scrCoords1=convertXY(origX1,origY1,WIDTH)
       scrCoords2=convertXY(origX2,origY2,WIDTH)
       t.color(col)
       t.penup()
       t.goto(scrCoords1)
       t.pendown()
       t.goto(scrCoords2)
       

def loadStars(filename, t): 
       starDict={}
       f=open(filename) #reads lines from txt
       line=f.readlines()
       bnessS=0 #let brightnessS = 0
       bnessX=0
       bnessY=0
       brightest=""
       for i in range(0,len(line)): #splits the lines up
              lineSplit=line[i].split(" ")
              origX=float(lineSplit[0]) #assign values for original x,y
              origY=float(lineSplit[1])
              bness=float(lineSplit[4]) #assign values for brightness
              drawStar(origX,origY,t,bness,"yellow") #calls drawstar to draw stars at these coords
              if len(lineSplit)>6:
                     newStr="" #create list for names of stars
                     for i in range(6,len(lineSplit)):
                            newStr=newStr+" "+lineSplit[i]
                            newStr=newStr.strip()
                     names=newStr.split("; ")
                     #print(names)
                     for elem in names: #creates dictionary keys and values
                            starDict[elem]=(origX,origY)
                     if bnessS<bness: #finds the brightest star, spose 0<current star's brightness
                            bnessS=bness #now the brightest star is this current one
                            bnessX=origX #use its x,y coords
                            bnessY=origY
                            brightXY=convertXY(bnessX,bnessY,WIDTH) #found coords for brightest star, now converts their coords
                            brightest=elem #gives brightest star name
       t.penup()
       t.goto(-300,300)
       t.pendown()
       t.color("white")
       t.write("The brightest star is:"+brightest) #tells us the brightest star
              
       return starDict
              
def drawConstellation(dictStars, constelFilename, t):
       f=open(constelFilename)
       line=f.readlines() 
       for i in range(0,len(line)): #draws constellations based off of txt files
              conSplit=line[i].split(",") 
              conSplit[1]=conSplit[1].strip()
              coords1=dictStars.get(conSplit[0])
              coords2=dictStars.get(conSplit[1]) 
              drawLine(coords1[0],coords1[1],coords2[0],coords2[1],t,"white")#calls drawLine to draw lines between stars
              t.hideturtle()
                    
def main():
       
       # Create screen and turtle
       import turtle
       scr = turtle.Screen()
       scr.bgcolor("darkblue")
       t=turtle.Turtle()      
       
       scr.tracer(0) # do not update the screen

       dictStars=loadStars("stars.txt",t)

       # Read constellation files (assumes they are in the current directory)
       import glob 
       listFiles = glob.glob("*_lines.txt")
       for filename in listFiles:
           #print(filename)
           drawConstellation(dictStars,filename,t)
           # Call draw constellations here
           
           
       scr.update() # update the screen
       scr.tracer(10)

main()   # call main


