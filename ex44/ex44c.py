class Parent(object):
    def altered(self):
        print "Parent altered()"

class Child(Parent):
    def altered(self):
        print "Child, befrot parent altered()"
        super(Child, self).altered()
        print "child after parent altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()
