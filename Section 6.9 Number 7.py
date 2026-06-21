# ----------------------------------------
# Program:   6.9 Exercise 7
# Author:    ynvj
# Name:      Jovanny Cano
# Date:      06/20/2026
# ----------------------------------------
import sys
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds #3600 is the amount of seconds in an hour
                                                 #60 is the amount of seconds in a minute

test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
