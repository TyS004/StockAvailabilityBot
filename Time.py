import time

class PgrmTime:

    def __init__(self):
        self.startTime = time.mktime(time.gmtime(time.time()))
        self.endTime = time.mktime(time.gmtime(time.time()))

    def timeSinceStart(self):
        self.endTime = time.mktime(time.gmtime(time.time()))
        deltaTime = self.endTime - self.startTime

        return deltaTime
