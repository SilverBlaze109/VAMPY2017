import turtle as t


def triangle(size):
	t.speed(1)
	t.forward(size)
	t.right(120)
	t.forward(size)
	t.right(120)
	t.forward(size)
	t.right(120)

triangle(100)
t.clear()
triangle(150)

t.exitonclick()
