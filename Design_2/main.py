from turtle import *
import colorsys as sr
title("Psychedelic Snake Design")
bgcolor('black')
tracer(200)

def draw():
    h = 0
    n = 20
    up()
    goto(0,30)
    down()
    pensize(5)
    for i in range(300):
        c = sr.hsv_to_rgb(h,1,1)
        h += 1/n
        color(c)
        fd(10)
        circle(i,6,20)
        for j in range(500):
            lt(971)
            circle(i*.1,j,steps=2)
            circle(i,2)
draw()
done()