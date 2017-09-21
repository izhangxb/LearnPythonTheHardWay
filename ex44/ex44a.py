class Parent(object):
    def implicit(self):
        print "Parent implicit()"

class CHild(Parent):
    pass

dad = Parent()
son = CHild()

dad.implicit()
son.implicit()