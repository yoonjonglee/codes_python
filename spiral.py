import turtle as t

def spiral(sp_len):
    if sp_len <= 5:
        return
    else:
        t.forward(sp_len)
        t.right(90)
        spiral(sp_len-5)

t.speed(1)
spiral(300)
t.hideturtle()
t.done()
