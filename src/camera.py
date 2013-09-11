class Camera:
    x = 0
    y = 0
    height = 0
    width = 0
    entitylock = None
    stickX = True
    stickY = False

    @staticmethod
    def update():
        if not Camera.entitylock:
            return
        if Camera.stickX: 
            Camera.x += Camera.entitylock.vel.x
        if Camera.stickY:
            Camera.y += Camera.entitylock.vel.y

