tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


for i in ["/","-","|","\\","|"]:
    print "%s\r" % i,

j = 0
while j < 10:
    j = j + 1
    print j


for k in range(5):
    for j in range(k):
        print "*",
    print "\r"
