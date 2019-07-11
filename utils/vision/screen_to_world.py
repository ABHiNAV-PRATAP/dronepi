import math


class Point():
    x = 0
    y = 0


class World:
    def toRad(self, deg):
        rad = deg * (math.pi/180)
        return rad

    def getWorldCoords(self, x, y, height):
        vfov = 60
        frameWidth = 0
        frameHeight = 0
        camera_height = height
        angle = 0

        worldPoint = Point()

        centerx = frameWidth/2
        centery = frameHeight/2
        h = x - centerx
        k = y - centery

        d = (frameHeight)/(2*math.tan(self.toRad(vfov/2)))
        vtheta = math.atan(((frameHeight/2) - (frameHeight - y))/d)
        htheta = vtheta + self.toRad(angle)
        worldx = camera_height/math.tan(htheta)

        D = math.sqrt((camera_height**2) + (worldx**2))
        ytheta = math.acos((d**2 + k**2)/(math.sqrt(d**2 + k**2) * math.sqrt(d**2 + h**2 + k**2)))

        worldy = D * math.tan(ytheta)

        worldPoint.x = worldx
        worldPoint.y = worldy

        return worldPoint
