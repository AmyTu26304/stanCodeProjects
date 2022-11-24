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
from breakoutgraphicsex import BreakoutGraphicsEx

# CONSTANT
FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3		  # Number of attempts
ACC = 1.005           # Acceleration constant after each break


def main():
    graphics = BreakoutGraphicsEx(brick_rows=10, brick_cols=10, paddle_width=100, num_lives=NUM_LIVES)
    lives = NUM_LIVES
    # graphics.set_lives(lives)
    # graphics.lives_board()
    vx = vy = 0
    you_win = 0
    bricks_removed = 0

    # Add the animation loop here!
    while lives != 0 and not you_win:
        pause(FRAME_RATE)

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
                # remove_heart = graphics.window.get_object_at(graphics.window.width - 1.5 * graphics.heart_r -
                #                                              lives * graphics.heart_r,
                #                                              graphics.window.height - 1 * graphics.heart_r)
                # graphics.window.remove(remove_heart)

            # Check for collisions
            x = graphics.ball.x
            y = graphics.ball.y
            r = graphics.ball_r

            upper_l = graphics.window.get_object_at(x, y)
            upper_r = graphics.window.get_object_at(x + r, y)

            lower_l = graphics.window.get_object_at(x, y + r)
            lower_r = graphics.window.get_object_at(x + r, y + r)

            if upper_l and upper_r and lower_l and lower_r is None:
                pass

            elif upper_l is not None and upper_l is not graphics.paddle and upper_l is not graphics.board:
                graphics.window.remove(upper_l)
                bricks_removed += 1
                vy *= ACC
                graphics.set_score(graphics.ball.y)
                vy = -vy

            elif upper_r is not None and upper_r is not graphics.paddle and upper_r is not graphics.board:
                graphics.window.remove(upper_r)
                bricks_removed += 1
                vy *= ACC
                graphics.set_score(graphics.ball.y)
                vy = -vy

            elif lower_l is not None and lower_l is not graphics.paddle and lower_l is not graphics.board:
                graphics.window.remove(lower_l)
                bricks_removed += 1
                graphics.set_score(graphics.ball.y)
            elif lower_r is not None and lower_r is not graphics.paddle and lower_r is not graphics.board:
                graphics.window.remove(lower_r)
                bricks_removed += 1
                graphics.set_score(graphics.ball.y)

            elif lower_l is not None and lower_l is graphics.paddle:
                vy = -vy
            elif lower_r is not None and lower_r is graphics.paddle:
                vy = -vy

        else:
            vx = graphics.get_dx()
            vy = graphics.get_dy()

    if lives == 0:
        graphics.reset_ball()
        graphics.sorry()

    if you_win:
        graphics.reset_ball()
        graphics.congrats()


if __name__ == '__main__':
    main()
