class pid_controller:
    def __init__(self, kP, kD, kDT):

        self.kP = kP
        self.kD = kD
        self.kDT = kDT
        self.prevOffset = 0

    def updateOutput(self, currentPos, desiredPos):
        if desiredPos is None:
            print("E: no desired position set!")
            return -1

        offset = desiredPos - currentPos

        output = (offset * self.kP) + (self.kD * ((offset - self.prevOffset) / self.kDT))
        self.prevOffset = offset

        return output
