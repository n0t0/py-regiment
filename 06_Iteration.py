# Updating variables

x = 0
x = x + 1
print x

# While statemenet
def countdown(n):
    while n > 0:
        print n
        n = n-1
    print 'Fire in the hole!'

print countdown(5)


def sequence(n):
    while n != 1:
        print n,
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1

print sequence(10)


def print_n(s, n):
    while n > 0:
        print s
        n = n - 1

print_n('flood', 3)

# Break
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line

print 'Done!'

# Square roots

# Newton's method for computing square roots: y = (x + a/x) / 2

a = 4.0
x = 3.0
y = (x + a/x) / 2
print y

while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

# Iffo Iffanoff
# Algorithms

# n * 9 = n-1 for first digit 10-n for second digit
