class Ball:

    def __init__(self, mass):
        
        self.mass = mass
        self.image = 'hex'
        self.x = 0
        self.y = 0

    def drop(self):
        print('я повесился')
        self.y = 2

    def kick(self):
        print('я утопился')
        self.x += 1

    def fail(self):
        self.mass = self.mass - 0.1
    
ball = Ball(0.5)
ball.drop()
ball.kick()
ball.fail()
print(ball.y)