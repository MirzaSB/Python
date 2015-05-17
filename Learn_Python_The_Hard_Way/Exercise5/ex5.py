name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_kg = weight / 2.2
height_cm = height * 2.54
num = 1
third = 030

print "Let's talk about %s." % name
print "He's %d centimeterss tall." % height_cm
print "He's %d kilos heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "If I want to test the r format character, I am going to put %r in this line" % height_cm

print "I dont like the integer decimal. My fav number is %i" % num
print "Test Octal %o" % third
