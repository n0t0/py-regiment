def increment(time, seconds):
    time.second += seconds

    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# Exercise 5
# Write a correct version of increment that doesn’t contain any loops.

# Exercise 6
# Write a “pure” version of increment that creates and returns a new Time object
# rather than modifying the parameter.
