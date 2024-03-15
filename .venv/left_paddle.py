from right_paddle import RightPaddle


class LeftPaddle(RightPaddle):
    def __init__(self):
        super().__init__()
        self.setposition(-350, 0)
