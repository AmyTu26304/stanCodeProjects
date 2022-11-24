"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
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
HEART_RADIUS = 30      # Radius of the heart in lives board (in pixels)


class BreakoutGraphicsEx:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout',
                 num_lives=3):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.starter_label = None
        self.starter()

        # Lives
        self.heart_r = HEART_RADIUS
        self._lives = num_lives
        # self.lives_board()    # <3

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

        # Score
        self._score = 0
        self.board = GLabel(f"Score: {self._score}", x=0, y=self.window.height)
        self.board.font = "Helvetica-20-italic"
        self.window.add(self.board)

        # Score
    def set_score(self, y):
        if self.b_offset < y < self.b_offset + 2 * (self.b_h + self.b_space):
            self._score += 50
        if self.b_offset + 2 * (self.b_h + self.b_space) < y < self.b_offset + 4 * (self.b_h + self.b_space):
            self._score += 40
        if self.b_offset + 4 * (self.b_h + self.b_space) < y < self.b_offset + 6 * (self.b_h + self.b_space):
            self._score += 30
        if self.b_offset + 6 * (self.b_h + self.b_space) < y < self.b_offset + 8 * (self.b_h + self.b_space):
            self._score += 20
        else:
            self._score += 10

        self.board.text = "Score: " + str(self._score)

    def reset_ball(self):
        self.ball.x = (self.window.width - self.ball_r)/2
        self.ball.y = (self.window.height - self.ball_r)/2
        self.move_or_not = 0
        self.__dx = 0
        self.__dy = 0

    # def set_lives(self, x):
    #     self._lives = x

    def lives_board(self):
        for i in range(self._lives):
            heart = GPolygon()
            heart.add_vertex(
                (self.window.width - 1.5 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 1 * HEART_RADIUS))
            heart.add_vertex(
                (self.window.width - 1.25 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 1.3 * HEART_RADIUS))
            heart.add_vertex(
                (self.window.width - 1 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 1 * HEART_RADIUS))
            heart.add_vertex(
                (self.window.width - 0.75 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 1.3 * HEART_RADIUS))
            heart.add_vertex(
                (self.window.width - 0.5 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 1 * HEART_RADIUS))
            heart.add_vertex(
                (self.window.width - 1 * HEART_RADIUS - i * HEART_RADIUS, self.window.height - 0.4 * HEART_RADIUS))

            heart.filled = True
            heart.color = "pink"
            heart.fill_color = "pink"
            self.window.add(heart)

    def starter(self):
        self.starter_label = GLabel("Click to start")
        self.starter_label.font = "Helvetica-20-bold"
        self.starter_label.color = "orange"
        self.window.add(self.starter_label, x=(self.window.width - self.starter_label.width)/2, y=self.window.height/1.5)

    def congrats(self):
        win_label = GLabel("You win!")
        win_label.font = "Helvetica-30-bold"
        self.window.add(win_label, x=(self.window.width - win_label.width)/2, y=self.window.height/2.5)

    def sorry(self):
        win_label = GLabel("No lives left :(")
        win_label.font = "Helvetica-30-bold"
        self.window.add(win_label, x=(self.window.width - win_label.width)/2, y=self.window.height/2.5)

    def move_ball(self, mouse):
        if not self.move_or_not:
            self.move_or_not = 1
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.window.remove(self.starter_label)

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
        for i in range(0, self.b_col):
            for j in range(0, self.b_row):
                brick = GRect(self.b_w, self.b_h, x=self.b_w * i + self.b_space * i,
                              y=self.b_offset + self.b_h * j + self.b_space * j)
                brick.filled = True

                color_row = self.b_row // 5
                if 0 <= j < color_row:
                    brick.fill_color = "firebrick"
                    brick.color = "firebrick"
                elif color_row <= j < 2 * color_row:
                    brick.fill_color = "indianred"
                    brick.color = "indianred"
                elif 2 * color_row <= j < 3 * color_row:
                    brick.fill_color = "rosybrown"
                    brick.color = "rosybrown"
                elif 3 * color_row <= j < 4 * color_row:
                    brick.fill_color = "salmon"
                    brick.color = "salmon"
                else:
                    brick.fill_color = "lightpink"
                    brick.color = "lightpink"

                self.window.add(brick)
