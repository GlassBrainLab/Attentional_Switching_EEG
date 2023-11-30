#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Thu Nov 30 12:24:10 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'SurveyTask'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s-%s_%s_%s' % (expInfo['participant'], expInfo['session'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/hsun11/Documents/GlassBrainLab/AttentionalSwitching/Task/2DTask/Attentional_Switching_EEG/AnxietySurveyTask/SurveyTask_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
win.allowStencil = True
form = visual.Form(win=win, name='form',
    items='SCAARED_form.xlsx',
    textHeight=0.03,
    font='Open Sans',
    randomize=False,
    style='dark',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1.5, 0.85),
    pos=(0, 0.05),
    itemPadding=0.05
)
done_button = visual.ButtonStim(win, 
    text='Click here when done', font='Helvetica',
    pos=(0.5, -0.45),
    letterHeight=0.03,
    size=(0.5, 0.09), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='done_button'
)
done_button.buttonClock = core.Clock()
footer = visual.TextStim(win=win, name='footer',
    text='Please answer every question.',
    font='Helvetica Neue',
    pos=(-0.45, -0.45), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [form, done_button, footer]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *form* updates
    if form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        form.frameNStart = frameN  # exact frame index
        form.tStart = t  # local t and not account for scr refresh
        form.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
        form.setAutoDraw(True)
    
    # *done_button* updates
    if done_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        done_button.frameNStart = frameN  # exact frame index
        done_button.tStart = t  # local t and not account for scr refresh
        done_button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_button, 'tStartRefresh')  # time at next scr refresh
        done_button.setAutoDraw(True)
    if done_button.status == STARTED:
        # check whether done_button has been pressed
        if done_button.isClicked:
            if not done_button.wasClicked:
                done_button.timesOn.append(done_button.buttonClock.getTime()) # store time of first click
                done_button.timesOff.append(done_button.buttonClock.getTime()) # store time clicked until
            else:
                done_button.timesOff[-1] = done_button.buttonClock.getTime() # update time clicked until
            if not done_button.wasClicked:
                if form.complete:
                    continueRoutine = False
                else:
                    footer.setText('Please make sure you have answered every question.')
                    if np.array_equal(footer.color, [1,1,1]):
                        footer.color = 'lightgrey'
                    else:
                        footer.color = 'white'
                    continueRoutine = True
            done_button.wasClicked = True  # if done_button is still clicked next frame, it is not a new click
        else:
            done_button.wasClicked = False  # if done_button is clicked next frame, it is a new click
    else:
        done_button.wasClicked = False  # if done_button is clicked next frame, it is a new click
    
    # *footer* updates
    if footer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        footer.frameNStart = frameN  # exact frame index
        footer.tStart = t  # local t and not account for scr refresh
        footer.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(footer, 'tStartRefresh')  # time at next scr refresh
        footer.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
form.addDataToExp(thisExp, 'rows')
form.autodraw = False
thisExp.addData('done_button.started', done_button.tStartRefresh)
thisExp.addData('done_button.stopped', done_button.tStopRefresh)
thisExp.addData('done_button.numClicks', done_button.numClicks)
if done_button.numClicks:
   thisExp.addData('done_button.timesOn', done_button.timesOn)
   thisExp.addData('done_button.timesOff', done_button.timesOff)
else:
   thisExp.addData('done_button.timesOn', "")
   thisExp.addData('done_button.timesOff', "")
thisExp.addData('footer.started', footer.tStartRefresh)
thisExp.addData('footer.stopped', footer.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
