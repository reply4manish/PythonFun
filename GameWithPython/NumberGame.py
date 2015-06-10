#!/usr/bin/env python

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console



try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

numberoftrials=None
secret_number=None

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global numberoftrials
    
    if numberoftrials==7:
        secret_number=random.randrange(0,100)
    elif numberoftrials==10:
        secret_number=random.randrange(0,1000)
    else:
        secret_number=random.randrange(0,100)
        numberoftrials=7
        global gametype
        gametype='range100'
    
    
   
 
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global numberoftrials
    global gametype
    gametype='range100'
    numberoftrials=7
    new_game()
    


def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global numberoftrials
    global gametype
    gametype='range1000'
    numberoftrials=10
    new_game()
    
    
    
def input_guess(guess):
    # main game logic goes here	
    guess=int(guess)
    print "Guess was",guess
    global secret_number
    global numberoftrials
    global gametype
    if guess > secret_number:
        numberoftrials=numberoftrials-1
        print "wrong guess-Lower: trial left %d" % numberoftrials
    elif guess < secret_number:            
        numberoftrials=numberoftrials-1
        print "wrong guess-Higher: trial left %d" % numberoftrials
    else:
        print " bravo ..!! Right guess"
          
    if gametype == 'range100' and numberoftrials==0:
        print 'Total number of trials finished: initialising new game....'
        range100()
    elif gametype== 'range1000' and numberoftrials==0:
        print 'Total number of trials finished: initialising new game....'
        range1000()
    elif gametype == 'range100' and guess==secret_number:
        print 'You won ..!! Initializing new game'
        new_game()
    elif gametype == 'range1000' and guess==secret_number:
        print 'You won ..!! Initializing new game'
        new_game()        
      
        
# create frame
frame = simplegui.create_frame("Guess game",150,150)


# register event handlers for control elements and start frame
button1=frame.add_button("Guess between 0-100",range100,200)
button2=frame.add_button("Guess between 0-1000",range1000,200)
textinput=frame.add_input("Guess",input_guess,50)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
