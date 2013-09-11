class Camera:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.entitylock = None
        self.stickX = True
        self.stickY = False

    def update(self):
        if not self.entitylock:
            return
        if self.stickX: 
            self.x += self.entitylock.vel.x
        if self.stickY:
            self.y += self.entitylock.vel.y

