### Exercise 1
Write a function called _distance_between_points_ that takes two _Points_
as arguments and returns the distance between them.

### Exercise 2
Write a function named _move_rectangle_ that takes a _Rectangle_ and two numbers
named dx and dy. It should change the location of the rectangle by adding dx
to the x coordinate of corner and adding dy to the y coordinate of corner.

### Exercise 3  
Write a version of _move_rectangle_ that creates and returns a new _Rectangle_ instead of modifying the old one.

### Exercise 4
Write a function called _print_time_ that takes a _Time_ object and prints it in the form hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least two digits, including a leading zero if necessary.

### Exercise 5
Write a boolean function called _is_after_ that takes two _Time_ objects, **t1** and **t2**, and returns _True_ if **t1** follows **t2** chronologically and _False_ otherwise. Challenge: don’t use an if statement.

### Exercise 6

```
def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
```

Is this function correct? What happens if the parameter **seconds** is much greater than sixty?

Write a correct version of _increment_ that doesn’t contain any loops.

### Exercise 7
Write a “pure” version of _increment_ that creates and returns a new _Time_ object rather than modifying the parameter.

### Exercise 8

Rewrite _increment_ using _time_to_int_ and _int_to_time_.

```
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
```

```
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
```


### Exercise 7  

The datetime module provides *date* and *time* objects that are similar to the *Date* and *Time* objects in this chapter, but they provide a rich set of methods and operators. Read the documentation at http://docs.python.org/2/library/datetime.html.

1. Use the datetime module to write a program that gets the current date and prints the day of the week.
2. Write a program that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
3. For two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day. Write a program that takes two birthdays and computes their Double Day.
4. For a little more challenge, write the more general version that computes the day when one person is n times older than the other.
