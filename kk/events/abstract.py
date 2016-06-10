class EventAbstract(object):
    _enabled = False

    def __init__(self, ckb):
        self._ckb = ckb
        self._defaultColor = self._ckb.defaultColor

        ckb.sendCmd(self.enable)

    @property
    def events(self):
        return self._events

    @property
    def enable(self):
        return self._enable

    @property
    def disable(self):
        return self._disable

    def action(self, event):
        pass
