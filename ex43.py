# coding=utf-8
from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print " This scene is not configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print "\n------------"
            next_scene_game = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_game)


class Death(Scene):
    quips = [
        "YOu died . YOU kinda suck at this.",
        "Your mom would be pround...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1)]


class CentralCorridor():
    def enter(self):
        print "the gothons of planet percal #25 have invaded your ship and destroyed"
        print "your entire crew. you are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an escape pod"
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "a Gothon jumos out, red sacly skin, dark grimy teeth,and evil clown constume"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pull a weapon to blast you"

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Fothon."
            print "His clown consume is flowing and moving around his body ,which throws"
            print "off your aim. Your laser hits his costume his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            return "death"

        elif action == "dodge!":
            print "like a world class boxer you dodge, weave ,slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lycky for you they made you learn GOthon insults in the academy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fa sng, jura fur fave nebgag gur ubjfr, fur fvgf nebhaq gur ubhrr"
            print "The Gothon stops, tries not to laugh, then busts out laughing and can't move"
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return "central_corridor"


class LaserWeaponArmory(Scene):
    def enter(self):
        print "You do a dive roll into the Weapon Armory,crouch and scan the room"
        print "for more Gothons that might be hiding, It's dead quiet ,too quiet."
        print "YOu stand up and run to the far side of the room and find the "
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb, The code is 3digits."
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        print '能猜出来就见鬼了...',code
        guess = raw_input("[keypad]>")
        guesses = 0

        while guess != code and guesses < 10:# guess < 9
            print "BZZZZZEDDDDDD!"
            guesses += 1
            guess = raw_input("[keypad]>")
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out"
            print "You grap the neutron bomb and run as fast as you can to the"
            print " brdge where you must place it inthe right apot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print"ship from their ship and you die."
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print "You burst onto the Bridge with the netron destuct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.Each of them has an even uglier"
        print "clown consume than the last, They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off"

        action = raw_input("> ")

        if action == " throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap ofr the door. Tight as you drop it a "
            print "Gothon shoot s you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb, You die knowing they will probably blow up when "
            print "it goes off"
            return 'death'
        elif action == "slowly place the bomb":
            print " You point your balster at the bomb under your arm"
            print " and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door ,open it ,and then carefully"
            print "place the bomb on the floor. pointing your blaster at it."
            print "YO then jumo back through the door. punch the close button"
            print "and blast the lock through the door,punch the close button"
            print "and blast the lock so the Gothons can't get out"
            print " Now thaat the bomb is placed you run to the sescape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod befroe the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have tiem to look. There's 5pods, which one"
        print "do you take?"

        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")
        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print  "The pod excapes out into the void of sapce, then"
            print "implodes as the hull rupures, crushing your body"
            print "into jam jelly."
            return "death"
        else:
            print " YOu jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. At it files to the planet , you look"
            print "back and see your ship implode then explode like a "
            print "bright start, taking out the Gothon ship at the same"
            print "time, YOU WIN!"

            return 'finished'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
