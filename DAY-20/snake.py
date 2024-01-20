from turtle import Turtle
Starting_Positions = [(0,0), (-20,0), (-40,0)]
Move_Distance = 20
Up = 90
Left = 180
Down = 270
Right = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for postion in Starting_Positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(postion)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            nex_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, nex_y)
        self.segments[0].forward(Move_Distance)

    def up(self):
        if self.segments[0].heading() != Down:
            self.segments[0].setheading(Up)

    def left(self):
        if self.segments[0].heading() != Right:
            self.segments[0].setheading(Left)

    def down(self):
        if self.segments[0].heading() != Up:
            self.segments[0].setheading(Down)

    def right(self):
        if self.segments[0].heading() != Left:
            self.segments[0].setheading(Right)