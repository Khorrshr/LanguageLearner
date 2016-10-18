# -*- coding: utf-8 -*-
#Language Learner script v1.01 by Khorrshr A.

#service code
from random import choice as choice
from re import split as split
from os import chdir as chdir
workdir = 'C:\Python\Translator' #may be changed if installed somewhere else
chdir(workdir)


#take dictionaries from file and fit them into enfi and fien. Also saves their keys in lists
def init(translation_lang):
    tehfile = open(translation_lang,'r')
    enfi, fien = {}, {} #in-program dictionaries for eng-fin and fin-eng translations*
    enWordList, fiWordList = [], [] #in-program list of keys for eng-fin and fin-eng POPOUT translations*
    for line in tehfile:
        stripped_line = line.rstrip('\n')
        fi,en = split('-', stripped_line)
        enfi[en]=fi
        fien[fi]=en
        enWordList.append(en)
        fiWordList.append(fi)
    return enfi, fien, enWordList, fiWordList


#initialization improvement with choosing the file to load. lol is list of libraries (names of the files trunkated into readible format)
def load(lol):
    print 'Choose the Library to load, by pressing the corresponding number. To exit type QQQ'
    for i in range(len(lol)):
        print lol[i], ' - ', i
    while True:
        x = raw_input('Your choice:  ').lower()
        if x == 'qqq':
            print 'Loading aborted'
            break
        else:
            try:
                x = int(x)
            except:
                print 'Provide an integer Number'
                continue
        if x not in range(len(lol)):
            print 'Incorrect number'
        else:
            opens = lol[x]
            filename = opens + '.txt'
            print filename, 'loaded'
            print '\n******'
            return filename


#add new words to a file
def add(translation_lang):
    tehfile = open(translation_lang,'a')
    while True:
        en_word = raw_input('Enter the word in English: ')
        if en_word == 'qqq':
            break
        fi_word = raw_input('Enter Finnish translation for it: ')
        if fi_word == 'qqq':
            break
        new_string = en_word + '-' + fi_word + '\n'
        tehfile.write(new_string.lower())
        print 'Word ' + en_word + '/' + fi_word + ' successfully added'


#check translation. Order is chosen randomly
def randomPopOut(dicti,listik,mode): #legal dicti are enfi and fien. use only corresponding enWordList or fiWordlist with it as listik (list of keys to choose from)
                                    #mode is 1 for removing words which are correctly guessed and 0 for keeping them in the rotation
    totalCounter, correctCounter = 0, 0
    listi = listik[:] #that solves the issue with depleting original list of keys, which required a relaunch of script for second walkthrough
    print '(To exit the lesson type QQQ)\n******\n'
    while len(listi) > 0:
        randKey = choice(listi)
        print randKey.upper(),
        answer = raw_input().lower()
        if answer == 'qqq':
                print 'Your result is: ', correctCounter, '/', totalCounter
                break
        elif answer == dicti[randKey]:
            if mode == 1:
                listi.remove(randKey)
            print 'Correct!'
            correctCounter += 1
            totalCounter += 1
        else:
            print 'Mistake! ' + randKey.upper() + ' translates as ' + dicti[randKey].upper()
            totalCounter += 1
        if len(listi) == 0:
            print 'Your result is: ', correctCounter, '/', totalCounter
        print


#wrappers for easy randomPopOut calls
def enfi0():
    print '\nTranslate given English words into FINNISH\nInfinite mode (words may repeat even when guessed correctly)'
    randomPopOut(enfi,enWordList,0)

def fien0():
    print '\nTranslate given Finnish words into ENGLISH\nInfinite mode (words may repeat even when guessed correctly)'
    randomPopOut(fien,fiWordList,0)

def enfi1():
    print '\nTranslate given English words into FINNISH\nPopout mode (words correctly guessed will not appear again)'
    randomPopOut(enfi,enWordList,1)

def fien1():
    print '\nTranslate given Finnish words into ENGLISH\nPopout mode (words correctly guessed will not appear again)'
    randomPopOut(fien,fiWordList,1)


#console commands
def what(): #checks which library is active
    print translation_lang, 'is loaded'

def change(): #changes loaded library on the go. works well, yet dictionaries looks strange on manual request
    global translation_lang, enfi, fien, enWordList, fiWordList
    translation_lang = load(lol)
    enfi, fien, enWordList, fiWordList = init(translation_lang)

def greet():
    print '\nWelcome to "Language Learner" by Khorrshr A.\n'
    print 'Commands:\nrun() - to choose and start a lesson'
    print "what() - check which library is loaded\nchange() - change the loaded library\nhelp() - doesn't work. Nodoby will help you\n\n******\n"

def run(): #wrapper for lesson start with textual menu
    print '\nChoose learning mode:\n\nIn infinite mode same word can occur more than one time'
    print 'In popout mode the word which you succefully guessed is removed from the rotation. Lesson stops when you guessed all of them'
    print 'You can terminate the lesson anytime by typing QQQ\n'
    print 'From English into FINNISH (infinite mode) - 1\nFrom English into FINNISH (popout mode)   - 2'
    print 'From Finnish into ENGLISH (infinite mode) - 3\nFrom Finnish into ENGLISH (popout mode)   - 4\nQuit menu - QQQ'
    while True:
        x = raw_input('Your choice:  ').lower()
        if x == 'qqq':
            print 'Lesson aborted'
            break
        else:
            try:
                x = int(x)
            except:
                print 'Provide an integer Number'
                continue
        if x not in range(1, len(listOfLessons)+1):
            print 'Incorrect number'
        else:
            print '******'
            exec listOfLessons[x-1]
            break


def help(): #todo later
    print 'Nobody will help you!'

###Body
#enfi, fien, enWordList, fiWordList = '', '', '', '' #obsolete, but it was required to avoid some problems at the past
lol = ['unsorted','color','food','house','month','number','pronoun','time','verb','weather','week','lesson1'] #List of Libraries
listOfLessons = ['enfi0()','enfi1()','fien0()','fien1()']

greet()
change()
run()


#Below that line is different crap

##### Messing with change() function. uncomment next block in case of total fail and use as hardcoded option to initialize script manually (ctrl+R)
#translation_lang = load(lol)     #chooses languages used or theme of a dictionary.
#enfi, fien, enWordList, fiWordList = init(translation_lang) #*
#####


#####following block is obsolete, yet still working in mode==0 style. only a dictionary provided as agrument
#
#checks translation. words are chosen at random
#def translateRandom(dicti): #enfi and fien are legal arguments for ENG->FIN and FIN->ENG translations respectively
#    totalCounter, correctCounter = 0, 0
#    print '(To exit the program type QQQ)\n******\n'
#    while True:
#        randKey = choice(dicti.keys())
#        print randKey.upper(),
#        answer = raw_input().lower()
#        if answer == 'qqq':
#            print 'Your result is: ', correctCounter, '/', totalCounter
#            break
#        elif answer == dicti[randKey]:
#            print 'Correct!'
#            correctCounter += 1
#        else:
#            print 'Mistake! ' + randKey.upper() + ' translates as ' + dicti[randKey].upper()
#        totalCounter += 1
#        print
#####


#TODO

#test add() with a new version of a script

#write help() function with the description of all commands

#separate function may automatically collect words from all other files into one big dictionary

#use finnish unique letters in python

#add 3rd row with russian words. process them into new dictionaries on the INIT stage

#take files list from directory automatically and create a list (lol) of it

#solve the same-word-different-meaning issue
#write a cleanup for double entries in the file

#qqq on start gives an error. solve it

#fix so the window wont close in cmd after qqq. looks like done. try to do it without infinte loop
#start cmd maximized
#fck, finnish öä letters doesn't work in cmd. so only fin->eng modes will work correctly

#idea. introduce repeat() function and all other functions like enfi0() shld save their print texts to global variable. Repeat will reprint text from it on demand to remind the rules and mode

#change enfi files to fien


#
#Changelog:
#
#    1.01
#    Introduced changelog
#    Removed "fien_" preffix from filenaming convention until I decide to introduce new languages (i.e. probably forever)
