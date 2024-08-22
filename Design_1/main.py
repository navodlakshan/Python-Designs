import turtle as t
t.bgcolor('black')
t.speed(0)
t.hideturtle()

colors = ['orangered','deeppink','darkOrange','magenta']

for i in range(120):
    for c in colors:
        t.color(c)
        t.circle(230-i,100)
        t.lt(90)
        t.circle(230-i,100)
        t.rt(60)
        t.end_fill()
t.mainloop()