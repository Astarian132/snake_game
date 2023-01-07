import turtle

MOVE_SPEED = 20
TURN_DEGREES = 90
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 360


class Snake:
    def __init__(self):
        self.snake_lenght = 3
        self.snake_parts = []
        for i in range(self.snake_lenght):
            Snake.set_up(self, x=(0 - (i * 20)))
        self.head = self.snake_parts[0]

    def set_up(self, x):
        snake_part = turtle.Turtle()
        snake_part.penup()
        snake_part.color('white')
        snake_part.shape('square')
        snake_part.setpos(x, 0)
        self.snake_parts.append(snake_part)

    def body_location(snake_part):
        return snake_part.pos()

    def move(self):
        previous_pos = None
        for part_num in range(self.snake_lenght):
            cur_pos = Snake.body_location(self.snake_parts[part_num])
            if previous_pos == None:
                self.snake_parts[part_num].fd(MOVE_SPEED)
            else:
                self.snake_parts[part_num].goto(previous_pos)
            previous_pos = cur_pos

    def check_if_possible(self, turn):
        return abs(self.head.heading() - turn) == 90 or abs(self.head.heading() - turn) == 270

    def up(self):
        if Snake.check_if_possible(self, UP):
            self.head.setheading(UP)

    def left(self):
        if Snake.check_if_possible(self, LEFT):
            self.head.setheading(LEFT)

    def down(self):
        if Snake.check_if_possible(self, DOWN):
            self.head.setheading(DOWN)

    def right(self):
        if Snake.check_if_possible(self, RIGHT):
            self.head.setheading(RIGHT)

    def grow(self):
        self.snake_lenght += 1
        snake_part = turtle.Turtle()
        snake_part.penup()
        snake_part.color('white')
        snake_part.shape('square')
        self.snake_parts.append(snake_part)
