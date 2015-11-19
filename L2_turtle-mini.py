import turtle

# create an instance of a triangle
def draw_triangle(some_turtle):
	for i in range(1,4):
		some_turtle.forward(50)
		some_turtle.right(120)


def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("blue")

	#create the turtle davey - draw a triangle
	davey = turtle.Turtle()
	davey.setpos(0, 175)

	# create outer loop (petals)
	davey.fill(True)

	for i in range(1, 7):
		davey.color("red")
		davey.speed(20)
		davey.circle(75)
		davey.right(60)
	davey.fill(False)
		
	davey.shape("turtle")
	davey.color("black")
	davey.speed(20)
	
	# create a inner loop (seeds) that will iterate davey 72 times:
	for i in range(1,73):
		draw_triangle(davey)
		davey.right(5)


	# create downward line (stem)	
	davey.color("green")
	davey.right(90)
	davey.forward(400)
	where = davey.pos()
	
	davey.fill(True)

	# create right leaf
	davey.circle(120, -100)
	davey.right(80)
	davey.circle(120, -100)

	davey.goto(where)
	# create left leaf
	davey.circle(120, -100)
	davey.right(80)
	davey.circle(120, -100)
	davey.fill(False)
	
	window.exitonclick()



draw_shapes()


