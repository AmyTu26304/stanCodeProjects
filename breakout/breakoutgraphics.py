"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_w = paddle_width
        self.paddle_h = paddle_height
        self.paddle_o = paddle_offset
        self.paddle = GRect(self.paddle_w, self.paddle_h)
        self.paddle.filled = True
        self.paddle.x = window_width-self.paddle_w/2
        self.paddle.y = window_height - self.paddle_o - self.paddle_h
        self.window.add(self.paddle, x=self.paddle.x, y=self.paddle.y)

        # Center a filled ball in the graphical window
        self.ball_r = 2 * ball_radius
        self.ball = GOval(self.ball_r, self.ball_r, x=(window_width - self.ball_r)/2,
                          y=(window_height - self.ball_r)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        self.move_or_not = 0
        self.vx = 0
        self.vy = 0
        self.__dx = 0
        self.__dy = 0

        self.b_row = brick_rows
        self.b_col = brick_cols
        self.b_w = brick_width
        self.b_h = brick_height
        self.b_space = brick_spacing
        self.b_offset = brick_offset

        # Draw bricks
        self.build_bricks()

        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.move_ball)
        onmousemoved(self.move_paddle)

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball_r)/2
        self.ball.y = (self.window.height - self.ball_r)/2
        self.move_or_not = 0
        self.__dx = 0
        self.__dy = 0

    def move_ball(self, mouse):
        if not self.move_or_not:
            self.move_or_not = 1

            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def move_paddle(self, event):
        if event.x > self.window.width - self.paddle.width/2:       # mouse moves exceed the right edge of the window
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x < self.paddle.width/2:                         # mouse moves exceed the left edge of the window
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def build_bricks(self):
        for i in range(0, self.b_row):
            for j in range(0, self.b_col):
                brick = GRect(self.b_w, self.b_h, x=self.b_w * i + self.b_space * i,
                                   y=self.b_offset + self.b_h * j + self.b_space * j)
                brick.filled = True

                color_row = self.b_col // 5
                if 0 <= j < color_row:
                    brick.fill_color = "red"
                elif color_row <= j < 2 * color_row:
                    brick.fill_color = "orange"
                elif 2 * color_row <= j < 3 * color_row:
                    brick.fill_color = "yellow"
                elif 3 * color_row <= j < 4 * color_row:
                    brick.fill_color = "green"
                else:
                    brick.fill_color = "blue"

                self.window.add(brick)
