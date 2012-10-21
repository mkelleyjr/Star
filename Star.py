# Michael L. Kelley Jr.
# Star.py
# 10/21/2012
# Draw a star on the screen using turtle graphics

from turtle import *
color('blue', 'orange')
begin_fill()
while True:
	forward(275)
	left(205)
	if abs(pos()) < 1:
		break
end_fill()
done()

