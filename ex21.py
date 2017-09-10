def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACT %d + %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLY %d + %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDE %d + %d" % (a, b)
    return a / b


print " let's do some math with just functions!"

age = add(30, 50)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d height: %d weight:%d IQ:%d" % (age, height, weight, iq)

print "here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes :", what, "can you do it by hand?"
