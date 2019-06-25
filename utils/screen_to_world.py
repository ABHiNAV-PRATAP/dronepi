import math


class Point():
    x = 0
    y = 0


def toRad(deg):
    rad = deg * (math.pi/180)
    return rad


def getWorldCoords(x, y):
    vfov = 0
    frameWidth = 0
    frameHeight = 0
    camera_height = 0
    angle = 0

    worldPoint = Point()

    centerx = frameWidth/2
    centery = frameHeight/2
    h = x - centerx
    k = y - centery

    d = (frameHeight)/(2*math.tan(toRad(vfov/2)))
    vtheta = math.atan(((frameHeight/2) - (frameHeight - y))/d)
    htheta = vtheta + toRad(angle)
    worldx = camera_height/math.tan(htheta)

    D = math.sqrt((camera_height**2) + (worldx**2))
    ytheta = math.acos((d**2 + k**2)/(math.sqrt(d**2 + k**2) * math.sqrt(d**2 + h**2 + k**2)))

    worldy = D * math.tan(ytheta)

    worldPoint.x = worldx
    worldPoint.y = worldy

    return worldPoint
