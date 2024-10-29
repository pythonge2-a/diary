

class Foo:
    pass

class Bar:
    pass


class Ball:
    def __init__(self, color='red'):
        self.color = color
        self.default_pressure = 1.3
        self.pressure = 0

    def inflate(self):
        self.pressure = self.default_pressure
        print('The ball is inflated')

def create_ball():
    ball1 = Ball('blue')
    ball2 = Ball()
    ball1.color = 'red'
    ball2.color = 'green'
    return ball