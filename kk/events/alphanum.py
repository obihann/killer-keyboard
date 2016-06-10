import string
import time
import threading

from queue import Queue

import kk.events.abstract as abstract

class AlphaNum(abstract.EventAbstract):
    _keyColor = "00ff00"
    _q = Queue()

    def __init__(self, ckb):
        letters = string.ascii_lowercase[:26]

        self._events = ["key +%s" % x for x in letters]
        self._enable = "@2 notify %s" % " ".join(["%s:on" % x for x in letters])
        self._disable = "@2 notify %s" % " ".join(["%s:off" % x for x in letters])

        for i in range(4):
            self._t = threading.Thread(target=self._worker)
            self._t.daemon = True
            self._t.start()

        super().__init__(ckb)

    def _worker(self):
        while True:
            event = self._q.get()
            eventPieces = event.split(" ")
            key = eventPieces[1].lstrip("+")

            self._ckb.sendCmd("rgb %s:%s" % (key.strip("\n"), self._keyColor))
            time.sleep(.5)
            self._ckb.sendCmd("rgb %s:%s" % (key[0], self._defaultColor))

            self._q.task_done()

    def action(self, event):
        self._q.put(event)
