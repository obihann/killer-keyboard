import kk.events.abstract as abstract

class Caps(abstract.EventAbstract):
    _capsColor = "ff0000"
    _events = ["key +caps"]
    _enable = "@2 notify caps:on"
    _disable = "@2 notify caps:off"

    def action(self, event):
        self._enabled = not self._enabled

        if self._enabled is True:
            self._ckb.sendCmd("rgb %s" % self._capsColor)
        else:
            self._ckb.sendCmd("rgb %s" % self._defaultColor)
