i = 0
numbers = []

while i < 6:
    print "at the top i is %d" % i
    numbers.append(i)

    i += 1
    print "numbers now :", numbers
    print "at the bottom i is %d" % i

print "the number is "

for num in numbers:
    print num


def circle(top_limit):
    j = 0
    while j < top_limit:
        print "at the top j is %d" % j
        numbers.append(j)

        j += 1
        print "numbers now :", numbers
        print "at the bottom j is %d" % j

circle(5)