# coding=utf-8
from sys import exit

def gold_room():
    global how_much
    print "This room is full of gold, how much do you take?"

    next = raw_input(">")
    if isDigit(next):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much<50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print " The bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "How are you going to move the bear?"
    bear_moved = False
    while True:
        next = raw_input(">")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print "the bear has moved form the door. you can go through it now"
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print " I got no idea what that means"

def cthulhu_room():
    print " Here you see the great evil Cthulhu"
    print " He, it ,whatever at you and you go insane"
    print "Do you flee for your life or eat your head?"

    next = raw_input(">")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why,".Good job!"
    exit(0)

def start():
    print " You are in a dark room"
    print " There is a door to your right and left"
    print " Which one do you take?"

    next = raw_input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumbled around the room untils you starve")


def isDigit(num):
    try:
        int(num)
        return True
    except:
        return False


start()




