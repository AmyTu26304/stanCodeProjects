"""
File: bouncing.ball.py
Name: Yi-Chen Tu (Amy Tu)
-------------------------
TODO: Bounce the ball after clicking the mouse, this program works for 3 times after the ball bounces out of the window.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
move_or_not = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(falling)
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    window.add(ball, START_X, START_Y)
    n = 3
    vy = 0

    while True:
        global move_or_not
        if n == 0:
            break

        if move_or_not:
            ball.move(VX, vy)
            pause(DELAY)

            if ball.y + SIZE + vy + GRAVITY > window.height and vy > 0:
                # if the next move of the ball falls beyond the lower edge
                vy_alt = window.height - ball.y - SIZE
                ball.move(VX, vy_alt)   # the ball reaches the floor
                pause(DELAY)
                ball.move(VX, -vy_alt)
                pause(DELAY)
                vy = -vy * REDUCE

            elif ball.y + SIZE == window.height and vy > 0:  # bounce when the ball exactly reaches the floor
                vy = -vy * REDUCE                            # velocity is reduced by the constant REDUCE

            else:
                vy += GRAVITY

            if ball.x >= window.width:    # the ball moves outside of the right edge of the window
                n -= 1                    # the counts reduced by 1
                window.add(ball, START_X, START_Y)      # the ball stops at the initial position
                vy = 0
                move_or_not = 0

        else:
            pause(50)


def falling(mouse):
    global move_or_not
    if not move_or_not:
        move_or_not = 1     # the ball starts falling once the mouse is clicked


if __name__ == "__main__":
    main()
