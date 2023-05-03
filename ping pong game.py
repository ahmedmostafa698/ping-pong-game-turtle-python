import turtle
wind=turtle.Screen()
wind.title("ping pong")
wind.bgcolor("black")
wind.setup(300,300)
wind.tracer()
#border
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

def render_border():
  pen.color("white")
  pen.width(5)
  pen.penup()

  left = -285
  right = 285
  top = 220
  bottom =- 220

  pen.goto(left, top)
  pen.pendown()
  pen.goto(right, top)
  pen.goto(right, bottom)
  pen.goto(left, bottom)
  pen.goto(left, top)
  pen.penup()
render_border()
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("white")
ball.goto(0,0)
ball.dx=2.5
ball.dy=2.5
#bat
bat=turtle.Turtle()
bat.speed(0)
bat.penup()
bat.shape("square")
bat.shapesize(1,5)
bat.color("red")
bat.goto(0,-200)
#score
score=turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
game_score=0
score.goto(0,240)

#Bricks

x1=-200
y1=200
arr=[]
for i in range(6):
  brick=turtle.Turtle()
  arr.append(brick)
  brick.speed(0)
  brick.penup()
  brick.shape("square")
  brick.shapesize(1,5)
  brick.color("blue")
  brick.goto(x1,y1)
  x1+=100
#paddle_function
def paddle_right():
  x=bat.xcor()
  x+=20
  bat.setx(x)
def paddle_left():
  x=bat.xcor()
  x-=20
  bat.setx(x)  
wind.listen()
wind.onkeypress(paddle_right,"Right")
wind.onkeypress(paddle_left,"Left")


#t1 = turtle.Turtle()
#t1.color("red")
#t1.up()
#t1.setpos(0, 50)
# t1.down()
# t1.circle(50)
# t1.clear()


#make_brick()

destroy=[]
while True:
  wind.update()
  #move ball
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)
  ball_x=int((ball.xcor()//100)+2)

  #ball hit brick
  if ball.ycor() > (brick.ycor())-20 and arr[ball_x] not   in destroy:
    ball.sety(170)
    ball.dy *=-1
    arr[ball_x].shapesize(1,1)
    arr[ball_x].setx(500)
    #arr[ball_x].sety(500)
    arr[ball_x].hideturtle()
    destroy.append(arr[ball_x])
    game_score+=1
    score.clear()
    score.write(f"score:{game_score}","center",font=('Arial', 15, 'normal'))
  
  # ball hit bordres 
  if ball.xcor() >280 :
    ball.setx(280)
    ball.dx *=-1
  if ball.xcor() <-280 :
    ball.setx(-280)
    ball.dx *=-1  
  if ball.xcor() <-280 :
    ball.setx(-280)
    ball.dx *=-1 
  #player  lose 
  if ball.ycor()<-350:
    ball.setx(0)
    ball.sety(0)
  #ball hit bat
  if ball.ycor() <-190 and ball.ycor() > -210 and( ball.xcor() <bat.xcor()+40) and (ball.xcor() >bat.xcor()-40): 
    ball.sety(-190)
    ball.dy *=-1
  #ball pass brick
  if ball.ycor()>300:
    ball.setx(0)
    ball.sety(0)
    ball.dy *=-1



'''
for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)
'''    