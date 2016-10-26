my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He weights %d pounds." % my_weight
print "Editorial comment."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# This line is tricky, try to get ti exactly right
print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

#additional stunt work
feet = my_height / 12
inches = my_height % 12

print "He's actually %d feet, %d inches tall." % (feet, inches)
