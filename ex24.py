print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t THE lovely world
with logic so firmlyu planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\twhere ther is none
"""

print "--------------"

print poem

print "--------------"

five = 10 - 2 + 3 - 6

print " this should be five : %s" % file


def secret_fromula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_fromula(start_point)

print "with a starting point of :%d" % start_point

print "we'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "we can also do that this way"
print "we'd have %d beans, %d jars,and %d crates." % secret_fromula(start_point)
