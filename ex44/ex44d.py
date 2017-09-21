class Parent(object):
    def override(self):
        print "Parent override()"

    def implict(self):
        print "Parent implicit()"

    def altered(self):
        print "Parent altered()"

class Child(Parent):
    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before parent altered()"
        super(Child, self).altered()
        print "Child, alter parent altered()"

dad = Parent()
son = Child()

dad.implict()
son.implict()

dad.override()
son.override()

dad.altered()
son.altered()