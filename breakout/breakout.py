"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a breakout project. The brick can be broken by the ball.
The paddle is moved by the mouse of the user to bounce the ball.
This project ends if the ball falls out of the bottom the window for 3 times,
or all of the bricks were removed within 3 attempts.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# CONSTANT
FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = vy = 0
    you_win = 0

    # Add the animation loop here!
    while lives != 0 and not you_win:
        pause(FRAME_RATE)

        # Check for bricks removed
        bricks_removed = 0
        for i in range(0, graphics.b_row):
            for j in range(0, graphics.b_col):

                if graphics.window.get_object_at(graphics.b_w * i + graphics.b_space * i,
                                                 graphics.b_offset + graphics.b_h * j + graphics.b_space * j) is None:
                    bricks_removed += 1

                if bricks_removed == graphics.b_row * graphics.b_col:       # all of the bricks were removed
                    you_win = 1

        # Move the ball
        if vx != 0 and vy != 0:
            graphics.ball.move(vx, vy)
            # Check
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                vx = -vx
            if graphics.ball.y <= 0:
                vy = -vy
            if graphics.ball.y + graphics.ball.height > graphics.window.height:     # the ball reaches the bottom edge
                graphics.reset_ball()
                vx = vy = 0
                lives -= 1

            # Check for collisions
            x = graphics.ball.x
            y = graphics.ball.y
            r = graphics.ball_r

            upper_l = graphics.window.get_object_at(x, y)
            upper = graphics.window.get_object_at(x + r / 2, y)
            upper_r = graphics.window.get_object_at(x + r, y)

            lower_l = graphics.window.get_object_at(x, y + r)
            lower_r = graphics.window.get_object_at(x + r, y + r)

            if upper and upper_l and upper_r and lower_l and lower_r is None:
                pass

            elif upper is not None and upper is not graphics.paddle and upper is not graphics.ball:
                graphics.window.remove(upper)
                vy = -vy

            elif upper_l is not None and upper_l is not graphics.paddle:
                graphics.window.remove(upper_l)
                vy = -vy

            elif upper_r is not None and upper_r is not graphics.paddle:
                graphics.window.remove(upper_r)
                vy = -vy

            elif lower_l is not None and lower_l is not graphics.paddle:
                graphics.window.remove(lower_l)
            elif lower_r is not None and lower_r is not graphics.paddle:
                graphics.window.remove(lower_r)

            elif lower_l is not None and lower_l is graphics.paddle:
                vy = -vy
            elif lower_r is not None and lower_r is graphics.paddle:
                vy = -vy

        else:
            vx = graphics.get_dx()
            vy = graphics.get_dy()

    if you_win:
        graphics.reset_ball()


if __name__ == '__main__':
    main()
