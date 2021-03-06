# Recursive Functions are Able to Call Themselves

def countdown(n):
    if n <= 0:
        print 'Fire in the hole!'
    else:
        print n
        countdown(n-1)
print countdown(5)


def print_n(s, n):
    if n <= 0:
        return
    print s
    print print_n(s, n-1)
print print_n('flood', 3)


s = 'Hello'
def print_n(s, n):
    if n <= 0:
        return
    print s
    print print_n(s, n-1)
print print_n(s, 3)

# Keyboard Input

name = raw_input("What's your name?\n")
print name

prompt = 'What was your speed?\n'
speed = raw_input(prompt)

print int(speed) # int() to convert string into integers
