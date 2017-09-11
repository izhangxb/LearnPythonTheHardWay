print "you enter a dark room with two doors.do you go through door #1 or door #2?"
door = raw_input(">")
if door == "1":
    print " there's a giant bear here eating a cheese cake. What do you do?"
    print "1. take the cake."
    print "2. Scream at the bear."

    bear = raw_input(">")
    if bear == "1":
        print "the bear eats your face off, good job!"
    elif bear == 2:
        print "the bear eats your legs off, good job!"
    else:
        print "well ,doing %s is probable better.Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at cthulhu's retina"
    print "1. blueberries."
    print "2. yellow jacket colthespins."
    print "3. understanding revolvers yelling meldoies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "your body surives powered by a mind of jello.good job!"
    else:
        print "the insanity rots your eyes into a pool of muck, good job!"
else:
    print " You stumble around and fall on a knife and die. Good job!"