class pid_controller:
    def __init__(self, kP, kD, kDT):

        self.kP = kP
        self.kD = kD
        self.kDT = kDT
        self.prevOffset = 0
        self.desiredPos = None

    def updateOutput(self, currentPos):
        if self.desiredPos is not None:
            return

        offset = self.desiredPos - currentPos

        output = (offset * self.kP) + (self.kD * ((offset - self.prevOffset) / self.kDT))
        self.prevOffset = offset

        return output

    def setDesiredPos(self, pos):
        self.desiredPos = pos
        self.prevOffset = 0
