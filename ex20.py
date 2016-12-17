from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# adding this for my own entertainment

linecount = file_len(input_file)


current_file = open(input_file)



print "%r lines." % linecount

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)


print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file),

current_line = current_line + 1
print_a_line(current_line, current_file),

current_line = current_line + 1
print_a_line(current_line, current_file),
