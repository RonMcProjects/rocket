# Relativistic time calculator

This is a Python (v3) translation of a program that appeared in the February 2002 issue of Sky & Telescope.  The original program was written in BASIC by Brian Tung.

It prompts the user for a distance in light-years and calculates the time it would take to get there accelerating at 1G for half the trip and decelerating at 1G for the other half.  It works out the time duration from the frame of reference of the stationary observer and that of the traveler.

The original BASIC source code can be seen here:
https://skyandtelescope.org/wp-content/uploads/rocket.bas

And a write-up by the author is here:
https://www.thefreelibrary.com/Relativistic+Travel%3A+To+the+Stars+in+a+Lifetime.-a097055409

## Usage
```
$ ./rocket.py 
Distance in light-years (0-100 million): 25000
Time on Earth: 000025001.938 years
Time on board: 000000019.686 years
    Top speed: 0.99999999700 c
```
You can also enter a fraction of a light-year for values < 1.
