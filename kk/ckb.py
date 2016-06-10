import sys
import time

class CKB(object):
    _notifyerFile = "/var/run/ckb1/notify2"
    _cmdFile = "/var/run/ckb1/cmd"

    def __init__(self, defaultColor = "ffffff"):
        self._defaultColor = defaultColor
        self.reset()

        try:
            self.notifier = open(self._notifyerFile, "r")
        except FileNotFoundError:
            self.sendCmd("notifyon 2")
            time.sleep(1)
            self.notifier = open(self._notifyerFile, "r")

    @property
    def defaultColor(self):
        return self._defaultColor

    def reset(self):
        self.sendCmd("active")
        self.sendCmd("@2 notify all:off")
        self.sendCmd("notifyoff 2")
        self.sendCmd("rgb ffffff")

    def sendCmd(self, msg):
        cmd = open(self._cmdFile, "w")
        cmd.write("%s \n" % msg)
        sys.stdout.flush()
        cmd.close()
