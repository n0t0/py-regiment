### Exercise 1  
 
Write a function called _square_ that takes a parameter named _t_, which is a turtle. It should use the turtle to draw a square.
Write a function call that passes _bob_ as an argument to _square_, and then run the program again.

### Exercise 2
Add another parameter, named _length_, to square. Modify the body so length of the sides is _length_, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for _length_.

### Exercise 3
The functions _lt_ and _rt_ make 90-degree turns by default, but you can provide a second argument that specifies the number of degrees. For example, _lt(bob, 45)_ turns _bob 45_ degrees to the left.
Make a copy of _square_ and change the name to _polygon_. Add another parameter named _n_ and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/_n_ degrees.

### Exercise 4
Write a function called _circle_ that takes a turtle, _t_, and radius, _r_, as parameters and that draws an approximate circle by invoking _polygon_ with an appropriate length and number of sides. Test your function with a range of values of _r_.
Hint: figure out the circumference of the circle and make sure that _length * n = circumference_.

Another hint: if _bob_ is too slow for you, you can speed him up by changing _bob.delay_, which is the time between moves, in seconds. _bob.delay = 0.01_ ought to get him moving.

### Exercise 5
Make a more general version of _circle_ called _arc_ that takes an additional parameter _angle_, which determines what fraction of a circle to draw. _angle_ is in units of degrees, so when _angle=360_, _arc_ should draw a complete circle.