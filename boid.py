WIDTH, HEIGHT = 600, 600


class Boid:
    def __init__(self, pos, velocity, acsseleration):
        self.pos = pos
        self.velocity = velocity
        self.acsseleration = acsseleration

    def update(self):
        self.pos += self.velocity
        self.velocity += self.acsseleration

        if self.pos[0, 0] < 0:
            self.pos[0, 0] = WIDTH - 1
        if self.pos[0, 0] >= WIDTH:
            self.pos[0, 0] = 0
        if self.pos[1, 0] < 0:
            self.pos[1, 0] = HEIGHT - 1
        if self.pos[1, 0] >= HEIGHT:
            self.pos[1, 0] = 0
